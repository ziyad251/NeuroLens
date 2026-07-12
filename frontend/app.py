import os
import sys
import streamlit as st

# Ensure frontend imports work when running:
# streamlit run frontend/app.py

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Theme
from frontend.ui.theme import apply_theme

# Pages
from frontend.app_pages.login import page_login
from frontend.app_pages.home import page_home
from frontend.app_pages.dashboard import page_dashboard
from frontend.app_pages.patient_registration import (
    page_patient_registration
)
from frontend.app_pages.mri_upload_prediction import (
    page_mri_upload_prediction
)
from frontend.app_pages.gradcam_visualization import (
    page_gradcam_visualization
)
from frontend.app_pages.clinical_assessment_form import (
    page_clinical_assessment_form
)
from frontend.app_pages.ai_report import page_ai_report
from frontend.app_pages.patient_history import page_patient_history
from frontend.app_pages.analytics_dashboard import (
    page_analytics_dashboard
)
from frontend.app_pages.settings import page_settings
from frontend.app_pages.contact import page_contact
from frontend.app_pages.about import page_about


# ----------------------------
# Streamlit Configuration
# ----------------------------
st.set_page_config(
    page_title="NeuroLens | Alzheimer's MRI AI",
    page_icon="N",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()


# ----------------------------
# Pages
# ----------------------------
PAGES = {
    "Home": page_home,
    "Login": page_login,
    "Dashboard": page_dashboard,
    "Contact": page_contact,
    "About": page_about,
    "Patient Registration": page_patient_registration,
    "MRI Upload & Prediction": page_mri_upload_prediction,
    "Grad-CAM Visualization": page_gradcam_visualization,
    "Clinical Assessment Form": page_clinical_assessment_form,
    "AI Report": page_ai_report,
    "Patient History": page_patient_history,
    "Analytics Dashboard": page_analytics_dashboard,
    "Settings": page_settings,
}


# ----------------------------
# Session Defaults
# ----------------------------
def ensure_session_defaults():
    defaults = {
        "authenticated": False,
        "role": "user",
        "active_patient_id": "",
        "active_patient_email": "",
        "last_prediction": None,
        "last_gradcam": "",
        "last_report_id": "",
        "ui_theme": "light",
        "active_page": "Home",
    }

    for key, value in defaults.items():
        st.session_state.setdefault(key, value)




# ----------------------------
# Sidebar Navigation (normal Streamlit)
# ----------------------------
def render_sidebar():
    role = st.session_state.get("role", "user")
    st.sidebar.markdown(
        """
        <div class="side-brand">
          <div class="side-brand-name">NeuroLens AI</div>
          <div class="side-brand-sub">Clinical MRI intelligence</div>
        </div>
        <div class="side-section">Workspace</div>
        """,
        unsafe_allow_html=True,
    )

    admin_only_pages = {
        "Analytics Dashboard",
        "Patient History",
        "AI Report",
        "Patient Registration",
        "Clinical Assessment Form",
        "Grad-CAM Visualization",
        "MRI Upload & Prediction",
    }

    pages = list(PAGES.keys())
    if role != "admin":
        pages = [p for p in pages if p in {"Home", "Dashboard", "Contact", "About", "Settings"}]

    # Ensure Login isn’t shown in sidebar
    pages = [p for p in pages if p != "Login"]

    for page_name in pages:
        active = st.session_state.get("active_page") == page_name
        st.sidebar.button(
            page_name,
            use_container_width=True,
            type="primary" if active else "secondary",
            key=f"nav_{page_name}",
            on_click=lambda pn=page_name: st.session_state.update({"active_page": pn}),
        )

    st.sidebar.markdown(
        f"""
        <div class="side-user">
          Signed in as
          <strong>{role}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.sidebar.button("Sign out", use_container_width=True):
        st.session_state.update(
            {"authenticated": False, "role": "user", "active_page": "Home"}
        )
        st.rerun()


# ----------------------------
# Main App
# ----------------------------
def main():

    ensure_session_defaults()

    if not st.session_state["authenticated"]:

        public_pages = {
            "Home",
            "Dashboard",
            "Contact",
            "About",
        }

        if (
            st.session_state["active_page"]
            not in public_pages
        ):
            st.session_state["active_page"] = "Login"

        st.markdown(
            """
            <style>
            [data-testid="stSidebar"]{
                display:none;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        PAGES[
            st.session_state["active_page"]
        ]()

        return

    # If user just logged in and is still on Login, show a default page
    if st.session_state.get("active_page") == "Login":
        st.session_state["active_page"] = "Home"

    # Normal Streamlit sidebar navigation
    render_sidebar()

    role = st.session_state.get("role")

    admin_only = {
        "Analytics Dashboard",
        "Patient History",
        "AI Report",
        "Patient Registration",
        "Clinical Assessment Form",
        "Grad-CAM Visualization",
        "MRI Upload & Prediction",
    }

    current = st.session_state["active_page"]

    if role != "admin" and current in admin_only:
        st.session_state["active_page"] = "Dashboard"

    PAGES[
        st.session_state["active_page"]
    ]()


# ----------------------------
# Entry Point
# ----------------------------
if __name__ == "__main__":
    main()
