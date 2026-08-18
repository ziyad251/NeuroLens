import os
from functools import lru_cache
from typing import Dict, List

from PIL import Image

# Matches your Colab `class_names` order:
# ["Mild Impairment", "Moderate Impairment", "No Impairment", "Very Mild Impairment"]
CLASSES: List[str] = [
    "Mild Impairment",
    "Moderate Impairment",
    "No Impairment",
    "Very Mild Impairment",
]


class ModelUnavailableError(RuntimeError):
    """Raised when real MRI inference cannot run without a trained model."""


def _device():
    import torch
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


@lru_cache(maxsize=1)
def _load_model():
    """
    Loads ResNet18 architecture and the state_dict from MODEL_PATH.

    Prediction must never continue without the trained model file.
    """
    from backend.config import get_settings

    settings = get_settings()
    model_path = settings.MODEL_PATH
    if not model_path or not os.path.exists(model_path):
        raise ModelUnavailableError(
            f"Trained model file is unavailable at '{model_path or 'MODEL_PATH not set'}'."
        )

    try:
        import torch
        from torchvision.models import resnet18

        model = resnet18(weights=None)
        model.fc = torch.nn.Linear(model.fc.in_features, 4, bias=True)

        state = torch.load(model_path, map_location="cpu", weights_only=True)
        model.load_state_dict(state, strict=True)
        model.eval()

        model.to(_device())
        return model
    except Exception as error:
        raise ModelUnavailableError(
            f"Trained model could not be loaded from '{model_path}'."
        ) from error


def _preprocess(pil_img: Image.Image):
    import torch
    import torchvision.transforms as T

    transform = T.Compose(
        [
            T.Resize((224, 224)),
            T.ToTensor(),
            T.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ]
    )
    x = transform(pil_img.convert("RGB")).unsqueeze(0)
    return x.to(_device())


def _risk_score_from_probs(probs) -> float:
    """
    Map class probabilities to a simple monotonic-ish risk score.
    Adjust if you have a different scoring rule.
    """
    import torch
    # Assign risk by impairment severity:
    # Mild(0) -> 55, Moderate(1) -> 85, No(2) -> 5, Very Mild(3) -> 25
    class_risk = torch.tensor([55.0, 85.0, 5.0, 25.0], device=probs.device)
    score = torch.sum(probs * class_risk).item()
    return float(round(score, 2))


def predict_stage_and_scores(image: Image.Image) -> Dict:
    import torch
    import torch.nn.functional as F

    model = _load_model()

    x = _preprocess(image)

    with torch.no_grad():
        logits = model(x)  # [1,4]
        probs = F.softmax(logits, dim=1)[0]  # [4]
        pred_idx = int(torch.argmax(probs).item())
        confidence = float(round(probs[pred_idx].item(), 4))
        risk = _risk_score_from_probs(probs)

    return {
        "predicted_stage": CLASSES[pred_idx],
        "confidence_score": confidence,
        "risk_score": risk,
        "raw_probs": [float(p.item()) for p in probs],  # used later for analytics/progression
        "predicted_index": pred_idx,
    }
