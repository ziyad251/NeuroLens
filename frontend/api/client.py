import base64
import os
from typing import Any, Dict, Optional, Tuple

import requests


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def health(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/health", timeout=20)
        r.raise_for_status()
        return r.json()

    def register_patient(self, name: str, age: int, gender: str = "", email: str = "") -> Dict[str, Any]:
        r = requests.post(
            f"{self.base_url}/api/patients/register",
            json={"name": name, "age": age, "gender": gender, "email": email},
            timeout=60,
        )
        r.raise_for_status()
        return r.json()

    def get_patient_history(self, patient_id: str) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/api/patients/{patient_id}/history", timeout=60)
        r.raise_for_status()
        return r.json()

    def predict_mri(
        self,
        mri_file_bytes: bytes,
        mri_filename: str,
        patient_id: str = "",
        patient_email: str = "",
        clinical_notes: str = "",
    ) -> Dict[str, Any]:
        files = {
            "mri_file": (mri_filename, mri_file_bytes),
        }
        data = {
            "patient_id": patient_id,
            "patient_email": patient_email,
            "clinical_notes": clinical_notes,
        }
        r = requests.post(f"{self.base_url}/api/predictions", files=files, data=data, timeout=120)
        if not r.ok:
            response_data = r.json() if r.content else {}
            if isinstance(response_data, dict) and response_data.get("error"):
                reasons = response_data.get("reasons") or []
                detail = f" {' '.join(reasons)}" if reasons else ""
                raise RuntimeError(f"{response_data['error']}{detail}")
        r.raise_for_status()
        return r.json()

    def generate_ai_report(
        self,
        patient_id: str,
        prediction: Dict[str, Any],
        clinician_notes: str = "",
    ) -> Dict[str, Any]:
        payload = {"patient_id": patient_id, "prediction": prediction, "clinician_notes": clinician_notes}
        r = requests.post(f"{self.base_url}/api/reports/generate", json=payload, timeout=120)
        r.raise_for_status()
        return r.json()

    def email_report(self, report_id: str, recipient_email: str) -> Dict[str, Any]:
        payload = {"report_id": report_id, "recipient_email": recipient_email}
        r = requests.post(f"{self.base_url}/api/reports/email", json=payload, timeout=120)
        data = r.json() if r.content else {}
        if r.ok:
            return data
        # 502 from backend includes {status, error, hint} for SMTP auth failures
        if isinstance(data, dict) and data.get("status"):
            return data
        r.raise_for_status()
        return data

    def stage_distribution(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/api/analytics/stage-distribution", timeout=60)
        r.raise_for_status()
        return r.json()

    def risk_trend(self) -> Dict[str, Any]:
        r = requests.get(f"{self.base_url}/api/analytics/risk-trend", timeout=60)
        r.raise_for_status()
        return r.json()


_default_client: Optional[ApiClient] = None


def get_api_client() -> ApiClient:
    global _default_client
    if _default_client is not None:
        return _default_client

    # Allow docker/compose to override
    base_url = os.getenv("API_BASE_URL", "http://localhost:5000").rstrip("/")
    _default_client = ApiClient(base_url)
    return _default_client
