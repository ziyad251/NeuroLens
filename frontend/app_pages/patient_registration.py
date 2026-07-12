import streamlit as st

from frontend.api.client import get_api_client


def page_patient_registration():
    st.markdown('<div class="eyebrow">Patients</div>', unsafe_allow_html=True)
    st.title("Register patient")
    st.markdown(
        '<p class="page-lead">Create a patient record before beginning MRI assessment or reporting.</p>',
        unsafe_allow_html=True,
    )
    api = get_api_client()

    form_column, context_column = st.columns([1.45, 1], gap="large")
    with form_column:
        with st.form("register_patient_form", clear_on_submit=False):
            name = st.text_input("Full name", placeholder="Patient full name")
            age = st.number_input("Age", min_value=0, max_value=120, step=1)
            gender = st.selectbox("Gender", ["", "Male", "Female", "Other"])
            email = st.text_input("Email address", placeholder="patient@example.com")
            submitted = st.form_submit_button(
                "Create patient record", type="primary", use_container_width=True
            )
    with context_column:
        st.markdown(
            """
            <div class="card">
              <span class="status-pill"><span class="status-dot"></span>Workflow step 1</span>
              <h3 style="margin: 1rem 0 .5rem;">What happens next?</h3>
              <p style="color: var(--muted); line-height: 1.6; margin: 0;">
                A patient ID is created and carried into MRI analysis, explainability
                review and report delivery.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if not submitted:
        return
    if not name.strip():
        st.error("Full name is required.")
        return
    if not email.strip() or "@" not in email.strip() or "." not in email.strip().split("@")[-1]:
        st.error("Please enter a valid email address.")
        return

    try:
        result = api.register_patient(
            name=name.strip(), age=int(age), gender=gender.strip(), email=email.strip()
        )
    except Exception as error:
        st.error(f"Registration failed: {error}")
        return

    patient = result.get("patient", {})
    patient_id = patient.get("patient_id", "")
    if patient_id:
        st.session_state["active_patient_id"] = patient_id
        st.session_state["active_patient_email"] = patient.get("email", email.strip())
        st.success(f"Patient created. Active patient ID: {patient_id}")
    else:
        st.success("Patient record created.")
