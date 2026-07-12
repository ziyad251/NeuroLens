import streamlit as st


def page_settings():
    st.session_state.setdefault("ui_theme", "light")
    st.markdown('<div class="eyebrow">Preferences</div>', unsafe_allow_html=True)
    st.title("Settings")
    st.markdown(
        '<p class="page-lead">Personalize the workspace appearance and review connection information.</p>',
        unsafe_allow_html=True,
    )

    current = st.session_state.get("ui_theme", "light")
    st.subheader("Appearance")
    st.caption("Choose the theme that is comfortable for your reading environment.")
    light, dark = st.columns(2, gap="medium")
    if light.button(
        "Light theme", use_container_width=True, type="primary" if current == "light" else "secondary"
    ):
        st.session_state["ui_theme"] = "light"
        st.rerun()
    if dark.button(
        "Dark theme", use_container_width=True, type="primary" if current == "dark" else "secondary"
    ):
        st.session_state["ui_theme"] = "dark"
        st.rerun()

    st.divider()
    st.subheader("System connection")
    st.markdown(
        """
        <div class="card">
          <span class="status-pill"><span class="status-dot"></span>Configured service</span>
          <p style="margin: 1rem 0 .3rem; color: var(--muted);">Backend endpoint</p>
          <strong>http://localhost:5000</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )
