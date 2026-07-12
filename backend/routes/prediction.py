from flask import Blueprint, jsonify, request
from PIL import Image

from backend.services.predictor import ModelUnavailableError, predict_stage_and_scores
from backend.services.gradcam import generate_gradcam_base64
from backend.services.mri_validator import validate_mri_image

bp = Blueprint("prediction", __name__)

def _do_predict():
    """
    Expected multipart/form-data:
    - patient_id (optional but recommended for saving history later)
    - clinical_notes (optional)
    - mri_file (required): image file
    """
    try:
        if "mri_file" not in request.files:
            return jsonify({"error": "mri_file is required"}), 400

        mri_file = request.files["mri_file"]
        patient_id = request.form.get("patient_id", "").strip()
        patient_email = request.form.get("patient_email", "").strip()
        clinical_notes = request.form.get("clinical_notes", "").strip()

        try:
            img = Image.open(mri_file.stream).convert("RGB")
        except Exception as e:
            return jsonify({"error": f"Invalid image: {str(e)}"}), 400

        validation = validate_mri_image(img)
        if not validation.accepted:
            return jsonify(
                {
                    "error": "Upload rejected: this image does not appear to be a compatible brain MRI scan.",
                    "code": "invalid_mri_image",
                    "reasons": validation.reasons,
                }
            ), 422

        try:
            pred = predict_stage_and_scores(img)
        except ModelUnavailableError as error:
            return jsonify({"error": str(error), "code": "model_unavailable"}), 503
        except Exception:
            return jsonify(
                {
                    "error": "The trained model could not complete prediction.",
                    "code": "inference_failed",
                }
            ), 500

        try:
            gradcam_b64 = generate_gradcam_base64(img, pred.get("predicted_index"))
        except Exception:
            gradcam_b64 = ""

        if patient_id and not patient_email:
            try:
                from backend.mongo.client import get_mongo
                from backend.mongo.repositories import PatientRepository

                _, db = get_mongo()
                repo = PatientRepository(db)
                patient_email = repo.get_patient_email(patient_id) or ""
            except Exception:
                pass

        prediction_id = None
        if patient_id:
            # Save prediction to MongoDB history
            try:
                from backend.mongo.client import get_mongo
                from backend.mongo.repositories import PatientRepository

                _, db = get_mongo()
                repo = PatientRepository(db)
                prediction_id = repo.upsert_prediction_history(
                    patient_id=patient_id,
                    patient_email=patient_email,
                    predicted_stage=pred["predicted_stage"],
                    confidence_score=float(pred["confidence_score"]),
                    risk_score=int(pred["risk_score"]),
                    gradcam_image_base64=gradcam_b64,
                    clinical_notes=clinical_notes,
                )
            except Exception:
                # If DB fails, still return prediction response to avoid client connection abort
                prediction_id = None

        response = {
            "patient_id": patient_id or None,
            "patient_email": patient_email or None,
            "prediction_id": prediction_id,
            "predicted_stage": pred.get("predicted_stage"),
            "confidence_score": pred.get("confidence_score"),
            "risk_score": pred.get("risk_score"),
            "gradcam_image_base64": gradcam_b64,
            "meta": {
                "input_format": getattr(mri_file, "mimetype", None),
                "clinical_notes_present": bool(clinical_notes),
                "model_inference": True,
                "gradcam_available": bool(gradcam_b64),
                "mri_validation": "passed",
            },
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@bp.post("/predict")
def predict():
    return _do_predict()

# Backwards-compatible route: POST /api/predictions
@bp.post("")
def predict_root():
    return _do_predict()
