from dataclasses import dataclass
from typing import List

import numpy as np
from PIL import Image


@dataclass(frozen=True)
class MRIValidationResult:
    accepted: bool
    reasons: List[str]


def validate_mri_image(image: Image.Image) -> MRIValidationResult:
    """
    Reject obvious out-of-domain uploads before MRI stage classification.

    This is a conservative plausibility check for exported 2D brain MRI slices,
    not a diagnostic validator or a replacement for a trained OOD detector.
    """
    if not isinstance(image, Image.Image):
        return MRIValidationResult(False, ["The upload is not a readable image."])

    if image.width < 96 or image.height < 96:
        return MRIValidationResult(False, ["The image is too small for MRI analysis."])

    rgb = np.asarray(image.convert("RGB").resize((224, 224)), dtype=np.float32)
    gray = np.asarray(image.convert("L").resize((224, 224)), dtype=np.float32)
    reasons = []

    channel_range = rgb.max(axis=2) - rgb.min(axis=2)
    color_pixel_ratio = float(np.mean(channel_range > 12.0))
    mean_channel_range = float(np.mean(channel_range))
    if color_pixel_ratio > 0.08 or mean_channel_range > 5.0:
        reasons.append("The uploaded image is not grayscale like an MRI slice.")

    if float(gray.std()) < 12.0:
        reasons.append("The image does not contain enough scan contrast.")

    border_width = max(8, int(min(gray.shape) * 0.10))
    border = np.concatenate(
        (
            gray[:border_width, :].ravel(),
            gray[-border_width:, :].ravel(),
            gray[:, :border_width].ravel(),
            gray[:, -border_width:].ravel(),
        )
    )
    dark_border_ratio = float(np.mean(border < 45.0))
    if dark_border_ratio < 0.42:
        reasons.append("The image does not have the expected dark MRI background.")

    foreground = gray > 30.0
    foreground_ratio = float(np.mean(foreground))
    if foreground_ratio < 0.06 or foreground_ratio > 0.78:
        reasons.append("The visible anatomy area is not consistent with a brain MRI slice.")
    elif foreground.any():
        ys, xs = np.nonzero(foreground)
        x_offset = abs(float(xs.mean()) - (gray.shape[1] - 1) / 2) / gray.shape[1]
        y_offset = abs(float(ys.mean()) - (gray.shape[0] - 1) / 2) / gray.shape[0]
        if x_offset > 0.18 or y_offset > 0.18:
            reasons.append("The scan anatomy is not centered as expected.")

    return MRIValidationResult(not reasons, reasons)
