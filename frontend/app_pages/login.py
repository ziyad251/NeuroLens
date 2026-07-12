import streamlit as st


def page_login():
    st.markdown(
        """
        <style>
        [data-testid="stHeader"], [data-testid="stToolbar"], footer {
            display: none;
        }
        [data-testid="stAppViewContainer"] > .main .block-container {
            max-width: 475px;
            margin: auto;
            padding: 3rem 2.5rem 2.4rem;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 28px;
            box-shadow: 0 24px 64px var(--shadow);
        }
        [data-testid="stAppViewContainer"] > .main {
            display: flex;
            min-height: 100vh;
            align-items: center;
        }
        .login-mark {
            height: 52px;
            width: 52px;
            display: grid;
            place-items: center;
            border-radius: 16px;
            margin-bottom: 1.35rem;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #fff;
            font-size: 1.35rem;
            font-weight: 750;
        }
        .login-title {
            color: var(--text);
            font-size: 1.85rem;
            line-height: 1.15;
            font-weight: 750;
            letter-spacing: -.045em;
            margin: 0 0 .45rem;
        }
        .login-subtitle {
            color: var(--muted);
            margin-bottom: 1.7rem;
            line-height: 1.55;
        }
        .login-footer {
            color: var(--muted);
            font-size: .84rem;
            text-align: center;
            padding-top: 1.2rem;
        }
        </style>
        <div class="login-mark">N</div>
        <div class="eyebrow">Secure access</div>
        <div class="login-title">Welcome to NeuroLens</div>
        <div class="login-subtitle">
          Sign in to review MRI analysis, explanations and patient reports.
        </div>
        """,
        unsafe_allow_html=True,
    )

    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")

    user_column, admin_column = st.columns(2, gap="small")
    user_login = user_column.button("User sign in", type="primary", use_container_width=True)
    admin_login = admin_column.button("Admin sign in", use_container_width=True)

    if user_login:
        if username.strip() and password.strip():
            st.session_state.update({"authenticated": True, "role": "user", "active_page": "Dashboard"})
            st.rerun()
        st.error("Enter your username and password.")

    if admin_login:
        if username.strip() == "admin" and password.strip() == "123456":
            st.session_state.update({"authenticated": True, "role": "admin", "active_page": "Dashboard"})
            st.rerun()
        st.error("Invalid administrator credentials.")

    st.markdown(
        """
        <div class="login-footer">
          Demo user access accepts any username and password.<br>
        </div>
        """,
        unsafe_allow_html=True,
    )
