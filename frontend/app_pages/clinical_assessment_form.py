import streamlit as st


def page_clinical_assessment_form():
    st.markdown('<div class="eyebrow">Clinical context</div>', unsafe_allow_html=True)
    st.title("Clinical assessment")
    st.markdown(
        '<p class="page-lead">Record clinician observations that will accompany the imaging result in the final report.</p>',
        unsafe_allow_html=True,
    )

    patient_id = st.text_input(
        "Patient ID",
        value=st.session_state.get("active_patient_id", ""),
        help="Associates this assessment with the active patient workflow.",
    )
    with st.form("clinical_assessment_form", clear_on_submit=False):
        left, right = st.columns(2, gap="large")
        with left:
            symptoms = st.text_area(
                "Reported symptoms (optional)",
                placeholder="Memory concerns, cognitive changes or family observations.",
                height=130,
            )
            cognitive_decline = st.slider("Cognitive decline", 0, 10, 5)
        with right:
            additional_findings = st.text_area(
                "Additional findings (optional)",
                placeholder="Clinical interpretation and follow-up notes.",
                height=130,
            )
            functional_impairment = st.slider("Functional impairment", 0, 10, 5)
        submitted = st.form_submit_button(
            "Save assessment", type="primary", use_container_width=True
        )

    if submitted:
        st.session_state["clinician_assessment"] = {
            "patient_id": patient_id.strip(),
            "symptoms": symptoms,
            "additional_findings": additional_findings,
            "cognitive_decline": cognitive_decline,
            "functional_impairment": functional_impairment,
        }
        st.success("Clinical assessment saved and ready for report generation.")
