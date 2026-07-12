import base64

import streamlit as st

from frontend.api.client import get_api_client


def page_mri_upload_prediction():
    st.markdown('<div class="eyebrow">Assessment</div>', unsafe_allow_html=True)
    st.title("MRI upload and prediction")
    st.markdown(
        '<p class="page-lead">Attach a scan to the active patient record and run AI-assisted staging with visual explainability.</p>',
        unsafe_allow_html=True,
    )

    api = get_api_client()
    details, scan = st.columns([1, 1.05], gap="large")
    with details:
        st.subheader("Patient details")
        patient_id = st.text_input(
            "Patient ID", value=st.session_state.get("active_patient_id", "")
        )
        patient_email = st.text_input(
            "Patient email", value=st.session_state.get("active_patient_email", "")
        )
        clinical_notes = st.text_area(
            "Clinical notes (optional)",
            placeholder="Add observations that may assist later report generation.",
            height=122,
        )
    with scan:
        st.subheader("MRI image")
        uploaded = st.file_uploader(
            "Upload PNG or JPEG scan",
            type=["png", "jpg", "jpeg"],
            accept_multiple_files=False,
        )
        st.caption("Only exported 2D brain MRI slices are accepted for analysis.")
        if uploaded:
            st.image(uploaded, caption=uploaded.name, use_column_width=True)

    run_prediction = st.button("Run prediction", type="primary", use_container_width=True)
    if run_prediction:
        if not uploaded:
            st.error("Please upload an MRI image.")
            return
        if not patient_id.strip() or not patient_email.strip():
            st.error("Patient ID and patient email are required before analysis.")
            return

        st.session_state["last_prediction"] = None
        st.session_state["last_gradcam"] = ""
        with st.spinner("Analyzing MRI scan..."):
            try:
                result = api.predict_mri(
                    mri_file_bytes=uploaded.getvalue(),
                    mri_filename=uploaded.name,
                    patient_id=patient_id.strip(),
                    patient_email=patient_email.strip(),
                    clinical_notes=clinical_notes,
                )
            except Exception as error:
                st.error(f"Prediction failed: {error}")
                return

        st.session_state["active_patient_id"] = patient_id.strip()
        st.session_state["active_patient_email"] = patient_email.strip()
        st.session_state["last_prediction"] = result
        st.session_state["last_gradcam"] = result.get("gradcam_image_base64", "")
        st.success("Analysis complete. Results have been added to this patient workflow.")

    result = st.session_state.get("last_prediction")
    if result:
        _render_result(result)


def _render_result(result):
    predicted_stage = result.get("predicted_stage") or "Unavailable"
    confidence = result.get("confidence_score")
    risk = result.get("risk_score")
    confidence_text = f"{float(confidence) * 100:.1f}%" if confidence is not None else "--"
    risk_text = f"{risk}/100" if risk is not None else "--"

    st.divider()
    st.subheader("Latest analysis")
    c1, c2, c3 = st.columns(3, gap="medium")
    c1.metric("Predicted stage", predicted_stage)
    c2.metric("Confidence", confidence_text)
    c3.metric("Risk score", risk_text)

    gradcam_data = result.get("gradcam_image_base64", "")
    if gradcam_data:
        st.subheader("Explainability preview")
        try:
            image_bytes = base64.b64decode(gradcam_data, validate=False)
            st.image(image_bytes, caption="Grad-CAM attention overlay", width=440)
        except Exception:
            st.info("The visual explanation could not be displayed for this scan.")
    else:
        st.info("A visual explanation is not available for this analysis.")
