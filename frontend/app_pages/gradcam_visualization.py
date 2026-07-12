import base64

import streamlit as st


def page_gradcam_visualization():
    st.markdown('<div class="eyebrow">Explainability</div>', unsafe_allow_html=True)
    st.title("Grad-CAM visualization")
    st.markdown(
        '<p class="page-lead">Review the attention overlay associated with the latest MRI prediction.</p>',
        unsafe_allow_html=True,
    )

    gradcam_data = st.session_state.get("last_gradcam", "") or ""
    if not gradcam_data:
        st.info("Run an MRI prediction first to view an explanation overlay.")
        return

    predicted = st.session_state.get("last_prediction", {}) or {}
    confidence = predicted.get("confidence_score")
    risk = predicted.get("risk_score")
    c1, c2, c3 = st.columns(3, gap="medium")
    c1.metric("Predicted stage", predicted.get("predicted_stage") or "Unavailable")
    c2.metric("Confidence", f"{float(confidence) * 100:.1f}%" if confidence is not None else "--")
    c3.metric("Risk score", f"{risk}/100" if risk is not None else "--")

    st.subheader("Attention overlay")
    st.image(base64.b64decode(gradcam_data), caption="Grad-CAM overlay", width=560)
    st.info(
        "Highlighted regions indicate where the model focused. Interpret this alongside clinical findings."
    )
