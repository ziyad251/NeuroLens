import streamlit as st
from typing import Dict, List, Tuple


def render_top_nav(items: List[Tuple[str, str]], brand: str = "Navigation") -> None:
    """
    items: list of (label, page_key) pairs
    page_key must match frontend/app.py PAGES dict keys.
    """
    st.markdown(
        """
        <style>
        .topnav-wrap {
            position: fixed;
            top: 12px;
            right: 18px;
            z-index: 999;
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 8px 10px;
            border-radius: 14px;
            background: rgba(17, 26, 46, 0.55);
            border: 1px solid rgba(36, 50, 74, 0.75);
            backdrop-filter: blur(10px);
        }

        .topnav-btn {
            appearance: none;
            border: 1px solid rgba(36, 50, 74, 0.85);
            background: rgba(17, 26, 46, 0.2);
            color: rgba(229, 231, 235, 0.95);
            border-radius: 12px;
            padding: 8px 12px;
            font-size: 13px;
            cursor: pointer;
            white-space: nowrap;
            transition: transform 120ms ease, border-color 120ms ease, background 120ms ease;
        }

        .topnav-btn:hover {
            transform: translateY(-1px);
            border-color: rgba(96, 165, 250, 0.8);
            background: rgba(96, 165, 250, 0.10);
        }

        .topnav-spacer {
            width: 6px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Render as HTML buttons that call back into Streamlit via a "click" form submission.
    # Streamlit cannot attach JS handlers reliably in this sandbox, so we render standard
    # st.button widgets for correctness and stable behavior.
    # Layout-wise we still keep the bar fixed using container CSS.
    st.markdown('<div class="topnav-wrap">', unsafe_allow_html=True)

    col_gap = 1
    for idx, (label, page_key) in enumerate(items):
        # Use keys to keep stable widget identity across reruns.
        if st.button(label, key=f"topnav_{page_key}", use_container_width=False):
            st.session_state["active_page"] = page_key
            st.rerun()

        if idx != len(items) - 1:
            st.markdown('<span class="topnav-spacer"></span>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
