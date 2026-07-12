import pandas as pd
import streamlit as st

from frontend.api.client import get_api_client


def page_dashboard():
    st.markdown('<div class="eyebrow">Overview</div>', unsafe_allow_html=True)
    st.title("Clinical dashboard")
    st.markdown(
        '<p class="page-lead">Monitor prediction volume and risk movement across recent MRI assessments.</p>',
        unsafe_allow_html=True,
    )

    api = get_api_client()
    try:
        dist = api.stage_distribution().get("distribution", [])
        trend = api.risk_trend().get("trend", [])
    except Exception:
        st.warning("Analytics are unavailable right now. Start the backend service to view live insights.")
        _empty_dashboard()
        return

    prediction_count = sum(int(row.get("count", 0)) for row in dist)
    stages_recorded = len(dist)
    latest_risk = trend[0].get("risk_score", 0) if trend else 0

    c1, c2, c3 = st.columns(3, gap="medium")
    c1.metric("Assessments", prediction_count)
    c2.metric("Stages observed", stages_recorded)
    c3.metric("Latest risk score", f"{latest_risk or 0}/100")

    left, right = st.columns(2, gap="large")
    with left:
        st.subheader("Stage distribution")
        if not dist:
            st.info("No predictions have been recorded yet.")
        else:
            dataframe = pd.DataFrame(dist)
            st.bar_chart(dataframe.set_index("stage")["count"], color="#087f77")
            st.dataframe(dataframe, use_container_width=True, hide_index=True)

    with right:
        st.subheader("Risk trend")
        if not trend:
            st.info("Risk history will appear after the first assessment.")
        else:
            trend_df = pd.DataFrame(trend)
            if "created_at" in trend_df.columns:
                trend_df = trend_df.sort_values(by="created_at")
            if "risk_score" in trend_df.columns:
                st.line_chart(trend_df["risk_score"], color="#2265c4")
            st.dataframe(
                trend_df[[col for col in ["predicted_stage", "risk_score", "created_at"] if col in trend_df]],
                use_container_width=True,
                hide_index=True,
            )

    st.caption("Dashboard metrics reflect stored prediction history and update as assessments are completed.")


def _empty_dashboard():
    c1, c2, c3 = st.columns(3, gap="medium")
    c1.metric("Assessments", "--")
    c2.metric("Stages observed", "--")
    c3.metric("Latest risk score", "--")
    st.info("Once the analytics service is connected, clinical trends will be displayed here.")
