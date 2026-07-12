import base64
import io
from typing import Optional

import numpy as np
from PIL import Image

from backend.services.predictor import _load_model, _preprocess


def _to_rgb_array_for_overlay(pil_img: Image.Image) -> np.ndarray:
    img = pil_img.convert("RGB").resize((224, 224))
    return np.array(img).astype(np.float32) / 255.0


def generate_gradcam_base64(image: Image.Image, target_index: Optional[int] = None) -> str:
    """
    Generate a Grad-CAM explanation for a real model inference.

    Explanation failure does not invalidate an already-completed prediction, but
    it must not be replaced with a generated demonstration image.
    """
    try:
        if not isinstance(image, Image.Image):
            return ""

        # Lazy imports to avoid torch/pytorch_grad_cam import-time stalls during Flask startup.
        import torch
        from pytorch_grad_cam import GradCAM
        from pytorch_grad_cam.utils.image import show_cam_on_image
        from pytorch_grad_cam.utils.model_targets import ClassifierOutputTarget

        model = _load_model()
        x = _preprocess(image)

        model.eval()
        with torch.no_grad():
            logits = model(x)
            probs = torch.softmax(logits, dim=1)[0]
            pred_idx = int(torch.argmax(probs).item())

        if target_index is None:
            target_index = pred_idx

        target_layers = [model.layer4[-1]]
        cam = GradCAM(model=model, target_layers=target_layers)
        targets = [ClassifierOutputTarget(target_index)]

        grayscale_cam = cam(input_tensor=x, targets=targets)[0]  # (H, W)

        rgb_img = _to_rgb_array_for_overlay(image)
        visualization = show_cam_on_image(rgb_img, grayscale_cam, use_rgb=True)

        out = Image.fromarray(visualization).convert("RGB").resize((224, 224))
        buf = io.BytesIO()
        out.save(buf, format="PNG")
        return base64.b64encode(buf.getvalue()).decode("utf-8")
    except Exception:
        return ""
