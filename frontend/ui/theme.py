import streamlit as st


def apply_theme():
    st.session_state.setdefault("ui_theme", "light")

    if st.session_state.get("ui_theme") == "dark":
        colors = {
            "bg": "#07111f",
            "bg_secondary": "#0e1c30",
            "panel": "rgba(14, 28, 48, 0.86)",
            "panel_solid": "#102036",
            "text": "#f1f5f9",
            "muted": "#9fb0c7",
            "border": "rgba(148, 163, 184, 0.18)",
            "primary": "#31b6aa",
            "primary_dark": "#13877f",
            "primary_soft": "rgba(49, 182, 170, 0.14)",
            "shadow": "rgba(2, 8, 23, 0.38)",
        }
    else:
        colors = {
            "bg": "#f4f8fb",
            "bg_secondary": "#edf5f7",
            "panel": "rgba(255, 255, 255, 0.92)",
            "panel_solid": "#ffffff",
            "text": "#10253d",
            "muted": "#607389",
            "border": "rgba(15, 45, 66, 0.10)",
            "primary": "#087f77",
            "primary_dark": "#076860",
            "primary_soft": "rgba(8, 127, 119, 0.09)",
            "shadow": "rgba(16, 37, 61, 0.08)",
        }

    st.markdown(
        f"""
        <style>
        :root {{
            --bg: {colors["bg"]};
            --bg-secondary: {colors["bg_secondary"]};
            --panel: {colors["panel"]};
            --panel-solid: {colors["panel_solid"]};
            --text: {colors["text"]};
            --muted: {colors["muted"]};
            --border: {colors["border"]};
            --primary: {colors["primary"]};
            --primary-dark: {colors["primary_dark"]};
            --primary-soft: {colors["primary_soft"]};
            --shadow: {colors["shadow"]};
            --radius: 20px;
        }}
        html, body, [class*="css"] {{
            font-family: "Inter", "Segoe UI", Arial, sans-serif;
            color: var(--text);
        }}
        .stApp {{
            background:
                radial-gradient(circle at 88% 4%, var(--primary-soft), transparent 29rem),
                radial-gradient(circle at 10% 98%, rgba(34, 101, 196, .07), transparent 25rem),
                var(--bg);
            color: var(--text);
        }}
        [data-testid="stHeader"] {{ background: transparent; }}
        [data-testid="stAppViewContainer"] > .main .block-container {{
            max-width: 1240px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }}
        h1, h2, h3, h4, h5, h6, p, li, label,
        [data-testid="stMarkdownContainer"], [data-testid="stMetricLabel"],
        [data-testid="stMetricValue"] {{ color: var(--text); }}
        h1 {{
            font-size: clamp(2rem, 3.1vw, 2.8rem) !important;
            letter-spacing: -.045em !important;
            font-weight: 750 !important;
        }}
        h2, h3 {{ letter-spacing: -.025em !important; }}
        [data-testid="stCaptionContainer"], .stCaption, small {{
            color: var(--muted) !important;
        }}
        hr {{
            border-color: var(--border) !important;
            margin: 1.7rem 0 !important;
        }}
        .eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: .45rem;
            padding: .38rem .72rem;
            margin-bottom: .8rem;
            border-radius: 999px;
            background: var(--primary-soft);
            color: var(--primary);
            font-size: .76rem;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
        }}
        .page-lead {{
            color: var(--muted) !important;
            max-width: 680px;
            font-size: 1.04rem;
            line-height: 1.65;
            margin-top: -.45rem;
            margin-bottom: 1.7rem;
        }}
        .card {{
            padding: 1.35rem 1.45rem;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            box-shadow: 0 12px 36px var(--shadow);
        }}
        .feature-card {{
            min-height: 128px;
            padding: 1.1rem 1.15rem;
            margin: .25rem 0 .7rem;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 18px;
        }}
        .feature-card strong {{
            display: block;
            color: var(--text);
            font-size: .98rem;
            margin-bottom: .35rem;
        }}
        .feature-card span {{
            color: var(--muted);
            font-size: .9rem;
            line-height: 1.5;
        }}
        .status-pill {{
            display: inline-flex;
            align-items: center;
            gap: .42rem;
            padding: .35rem .7rem;
            border-radius: 999px;
            background: var(--primary-soft);
            color: var(--primary);
            font-weight: 650;
            font-size: .8rem;
        }}
        .status-dot {{
            height: .48rem;
            width: .48rem;
            border-radius: 50%;
            background: var(--primary);
        }}
        div[data-testid="stMetric"] {{
            padding: 1rem 1.05rem;
            min-height: 104px;
            background: var(--panel);
            border: 1px solid var(--border);
            border-radius: 17px;
            box-shadow: 0 8px 24px var(--shadow);
        }}
        [data-testid="stMetricValue"] {{
            font-size: 1.68rem;
            font-weight: 700;
            letter-spacing: -.035em;
        }}
        [data-testid="stTextInputRootElement"],
        [data-baseweb="select"] > div,
        [data-testid="stFileUploaderDropzone"],
        textarea {{
            background: var(--panel-solid) !important;
            border-color: var(--border) !important;
            border-radius: 13px !important;
        }}
        input, textarea {{
            color: var(--text) !important;
            -webkit-text-fill-color: var(--text) !important;
        }}
        input::placeholder, textarea::placeholder {{
            color: var(--muted) !important;
        }}
        [data-testid="stTextInputRootElement"]:focus-within,
        [data-baseweb="select"] > div:focus-within,
        textarea:focus {{
            border-color: var(--primary) !important;
            box-shadow: 0 0 0 3px var(--primary-soft) !important;
        }}
        [data-testid="stFileUploaderDropzone"] {{ padding: 1.4rem !important; }}
        .stButton > button, .stDownloadButton > button,
        [data-testid="stFormSubmitButton"] button {{
            min-height: 2.85rem;
            border-radius: 13px !important;
            border: 1px solid var(--border) !important;
            background: var(--panel-solid) !important;
            color: var(--text) !important;
            font-weight: 650 !important;
            transition: transform .16s ease, box-shadow .16s ease, border-color .16s ease;
        }}
        .stButton > button:hover, .stDownloadButton > button:hover,
        [data-testid="stFormSubmitButton"] button:hover {{
            transform: translateY(-1px);
            border-color: rgba(8, 127, 119, .38) !important;
            box-shadow: 0 9px 22px var(--shadow);
            color: var(--primary) !important;
        }}
        .stButton > button[kind="primary"],
        [data-testid="stFormSubmitButton"] button[kind="primary"],
        .stDownloadButton > button[kind="primary"] {{
            border-color: transparent !important;
            background: linear-gradient(135deg, var(--primary), var(--primary-dark)) !important;
            color: #ffffff !important;
            box-shadow: 0 10px 22px rgba(8, 127, 119, .22);
        }}
        .stButton > button[kind="primary"]:hover,
        [data-testid="stFormSubmitButton"] button[kind="primary"]:hover {{
            color: #ffffff !important;
        }}
        [data-testid="stAlert"] {{
            border-radius: 15px;
            border: 1px solid var(--border);
        }}
        [data-testid="stDataFrame"], [data-testid="stTable"] {{
            border: 1px solid var(--border);
            border-radius: 16px;
            overflow: hidden;
        }}
        section[data-testid="stSidebar"] {{
            background: var(--panel-solid);
            border-right: 1px solid var(--border);
        }}
        section[data-testid="stSidebar"] > div {{ padding-top: 1.1rem; }}
        .side-brand {{
            padding: .45rem .2rem 1.15rem;
            border-bottom: 1px solid var(--border);
            margin-bottom: .85rem;
        }}
        .side-brand-name {{
            color: var(--text);
            font-size: 1.08rem;
            font-weight: 750;
            letter-spacing: -.03em;
        }}
        .side-brand-sub {{
            color: var(--muted);
            font-size: .77rem;
            margin-top: .18rem;
        }}
        .side-section {{
            color: var(--muted);
            letter-spacing: .1em;
            text-transform: uppercase;
            font-size: .67rem;
            font-weight: 700;
            margin: 1rem .25rem .45rem;
        }}
        section[data-testid="stSidebar"] .stButton > button {{
            width: 100%;
            min-height: 2.55rem;
            justify-content: flex-start;
            padding-left: .8rem;
            box-shadow: none;
            background: transparent !important;
        }}
        section[data-testid="stSidebar"] .stButton > button[kind="primary"] {{
            background: var(--primary-soft) !important;
            color: var(--primary) !important;
            border-color: transparent !important;
        }}
        .side-user {{
            padding: .8rem .85rem;
            margin-top: 1.4rem;
            border: 1px solid var(--border);
            border-radius: 14px;
            background: var(--bg);
            color: var(--muted);
            font-size: .82rem;
        }}
        .side-user strong {{
            display: block;
            color: var(--text);
            text-transform: capitalize;
            margin-top: .2rem;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
