import base64
import os

import streamlit as st

_ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
_WALLPAPER_PATH = os.path.join(_ASSETS_DIR, "home_brain_wallpaper.jpg")


def _brain_wallpaper_data_uri() -> str:
    with open(_WALLPAPER_PATH, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


def page_home():
    wallpaper_uri = _brain_wallpaper_data_uri()

    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] > .main .block-container {{
            max-width: 1180px;
            padding-top: 1.55rem;
        }}
        .hero {{
            position: relative;
            min-height: 470px;
            display: flex;
            align-items: flex-end;
            overflow: hidden;
            border-radius: 30px;
            padding: clamp(2rem, 6vw, 3.5rem);
            margin-bottom: 1.7rem;
            box-shadow: 0 22px 56px rgba(9, 31, 49, .16);
            background-image:
                linear-gradient(90deg, rgba(5, 18, 35, .92) 0%, rgba(5, 20, 38, .73) 44%, rgba(5, 20, 38, .30) 100%),
                linear-gradient(0deg, rgba(5, 18, 35, .68), transparent 56%),
                url("{wallpaper_uri}");
            background-size: cover;
            background-position: center;
        }}
        .hero-content {{ max-width: 590px; }}
        .hero .hero-kicker {{
            display: inline-flex;
            border: 1px solid rgba(119, 213, 202, .35);
            border-radius: 999px;
            padding: .42rem .78rem;
            color: #a6ece2;
            background: rgba(8, 127, 119, .22);
            font-size: .76rem;
            font-weight: 700;
            letter-spacing: .11em;
            text-transform: uppercase;
            margin-bottom: 1.1rem;
        }}
        .hero h1 {{
            margin: 0 0 .9rem !important;
            color: #ffffff !important;
            font-size: clamp(2.35rem, 4vw, 3.4rem) !important;
            line-height: 1.05;
        }}
        .hero p {{
            color: rgba(235, 244, 249, .84) !important;
            font-size: 1.03rem;
            line-height: 1.65;
            margin: 0;
        }}
        .home-heading {{
            margin: 1.55rem 0 .35rem;
            font-size: 1.33rem;
            font-weight: 700;
            letter-spacing: -.03em;
        }}
        </style>
        <section class="hero">
          <div class="hero-content">
            <div class="hero-kicker">MRI decision support</div>
            <h1>Clearer insight for cognitive care.</h1>
            <p>
              NeuroLens supports Alzheimer&apos;s screening with MRI stage prediction,
              explainability heatmaps and clinician-ready reporting in one focused workflow.
            </p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    primary, secondary, _ = st.columns([1.25, 1.25, 3.2], gap="small")
    if primary.button("Enter workspace", type="primary", use_container_width=True):
        st.session_state["active_page"] = "Login"
        st.rerun()
    if secondary.button("View dashboard", use_container_width=True):
        st.session_state["active_page"] = "Dashboard"
        st.rerun()

    st.markdown('<div class="home-heading">A connected assessment flow</div>', unsafe_allow_html=True)
    st.caption("Built for focused review, from imaging input through patient communication.")

    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        ("01  MRI analysis", "Upload an MRI scan and review predicted stage, confidence and risk indicators."),
        ("02  Visual evidence", "Inspect Grad-CAM overlays to understand regions informing the AI output."),
        ("03  Clinical report", "Combine assessment notes with results and deliver a structured PDF report."),
    ]
    for column, (title, description) in zip((c1, c2, c3), cards):
        column.markdown(
            f'<div class="feature-card"><strong>{title}</strong><span>{description}</span></div>',
            unsafe_allow_html=True,
        )

    st.info("This platform is a clinical decision-support prototype and does not replace professional diagnosis.")
