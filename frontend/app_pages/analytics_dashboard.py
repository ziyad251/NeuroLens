import pandas as pd
import streamlit as st

from frontend.api.client import get_api_client


def page_analytics_dashboard():
    st.markdown('<div class="eyebrow">Analytics</div>', unsafe_allow_html=True)
    st.title("Population insights")
    st.markdown(
        '<p class="page-lead">Explore recorded disease stage distribution and recent risk patterns across assessments.</p>',
        unsafe_allow_html=True,
    )
    api = get_api_client()

    left, right = st.columns(2, gap="large")
    with left:
        st.subheader("Disease stage distribution")
        try:
            distribution = api.stage_distribution().get("distribution", [])
            if distribution:
                dataframe = pd.DataFrame(distribution)
                st.bar_chart(dataframe.set_index("stage")["count"], color="#087f77")
                st.dataframe(dataframe, use_container_width=True, hide_index=True)
            else:
                st.info("No stage data available yet.")
        except Exception:
            st.warning("Stage distribution is currently unavailable.")

    with right:
        st.subheader("Risk trend")
        try:
            trend = api.risk_trend().get("trend", [])
            if trend:
                dataframe = pd.DataFrame(trend)
                if "risk_score" in dataframe.columns and len(dataframe) > 1:
                    st.line_chart(dataframe["risk_score"], color="#2265c4")
                st.dataframe(dataframe.head(20), use_container_width=True, hide_index=True)
            else:
                st.info("No risk observations available yet.")
        except Exception:
            st.warning("Risk trend is currently unavailable.")

    st.caption("Insights update from stored prediction history as new assessments are completed.")
