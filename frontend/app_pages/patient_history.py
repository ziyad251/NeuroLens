import pandas as pd
import streamlit as st

from frontend.api.client import get_api_client


def page_patient_history():
    st.markdown('<div class="eyebrow">Records</div>', unsafe_allow_html=True)
    st.title("Patient history")
    st.markdown(
        '<p class="page-lead">Retrieve previous MRI assessments and observe risk movement over time.</p>',
        unsafe_allow_html=True,
    )

    api = get_api_client()
    search, action = st.columns([3, 1], vertical_alignment="bottom")
    patient_id = search.text_input(
        "Patient ID",
        value=st.session_state.get("active_patient_id", ""),
        placeholder="Enter patient ID",
    )
    load_history = action.button("Load history", type="primary", use_container_width=True)
    if not load_history:
        return
    if not patient_id.strip():
        st.error("Patient ID is required.")
        return

    with st.spinner("Loading patient record..."):
        try:
            history = api.get_patient_history(patient_id.strip()).get("history", [])
        except Exception as error:
            st.error(f"History could not be loaded: {error}")
            return
    if not history:
        st.info("No previous assessments were found for this patient.")
        return

    dataframe = pd.DataFrame(history)
    st.subheader("Assessment timeline")
    if "risk_score" in dataframe.columns and len(dataframe) > 1:
        st.line_chart(dataframe["risk_score"], color="#087f77")
    st.dataframe(dataframe, use_container_width=True, hide_index=True)
