import streamlit as st


def page_contact():
    st.markdown('<div class="eyebrow">Support</div>', unsafe_allow_html=True)
    st.title("Contact the team")
    st.markdown(
        '<p class="page-lead">Need assistance with access, an assessment workflow or an integration? Our support channel is here to help.</p>',
        unsafe_allow_html=True,
    )

    email, phone = st.columns(2, gap="medium")
    email.markdown(
        """
        <div class="card">
          <div class="status-pill">Email support</div>
          <h3 style="margin: 1rem 0 .25rem;">support@example.com</h3>
          <p style="margin: 0; color: var(--muted);">For product access and technical questions.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    phone.markdown(
        """
        <div class="card">
          <div class="status-pill">Telephone</div>
          <h3 style="margin: 1rem 0 .25rem;">+1 (000) 000-0000</h3>
          <p style="margin: 0; color: var(--muted);">For urgent operational support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Replace these demonstration contact details before deploying the platform.")
