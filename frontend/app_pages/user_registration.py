import streamlit as st


def page_user_registration():
    st.title("User Registration")

    # Ensure defaults exist
    st.session_state.setdefault("registered", False)
    st.session_state.setdefault("user_profile", None)

    with st.form("user_registration_form", clear_on_submit=False):
        st.subheader("Create your account")

        full_name = st.text_input("Full Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        username = st.text_input("Username", placeholder="Choose a username")
        password = st.text_input("Password", type="password", placeholder="Create a password")
        confirm_password = st.text_input(
            "Confirm Password", type="password", placeholder="Re-enter your password"
        )

        submitted = st.form_submit_button("Register")

    if submitted:
        if not full_name.strip():
            st.error("Please enter your full name.")
            return
        if not email.strip():
            st.error("Please enter your email.")
            return
        if not username.strip():
            st.error("Please enter a username.")
            return
        if not password:
            st.error("Please enter a password.")
            return
        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        # Store registration locally in session_state (no backend for now)
        st.session_state["registered"] = True
        st.session_state["user_profile"] = {
            "full_name": full_name.strip(),
            "email": email.strip(),
            "username": username.strip(),
        }
        st.success("Registration successful. Please log in.")
        st.rerun()

    st.markdown("---")
    st.caption("Demo registration stores data in your session only (no backend persistence yet).")
