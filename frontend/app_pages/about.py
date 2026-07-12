import streamlit as st


def page_about():
    st.markdown('<div class="eyebrow">About</div>', unsafe_allow_html=True)
    st.title("Responsible imaging support")
    st.markdown(
        '<p class="page-lead">NeuroLens is an Alzheimer\'s MRI workflow prototype designed to organize AI outputs for clinical review.</p>',
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    features = [
        ("MRI staging", "Processes uploaded scans to present a predicted disease stage and confidence."),
        ("Explainability", "Displays Grad-CAM attention overlays for transparent model review."),
        ("Reporting", "Packages imaging output and clinical notes into downloadable documentation."),
    ]
    for column, (title, body) in zip((c1, c2, c3), features):
        column.markdown(
            f'<div class="feature-card"><strong>{title}</strong><span>{body}</span></div>',
            unsafe_allow_html=True,
        )

    st.info(
        "This prototype supports clinical review and research workflows. It is not a diagnostic device."
    )
