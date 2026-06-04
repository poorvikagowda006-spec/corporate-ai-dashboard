import streamlit as st
import pandas as pd

from analytics import (
    load_data,
    get_kpis,
    industry_summary,
    country_summary
)

from charts import (
    adoption_trend_chart,
    industry_chart,
    country_chart,
    investment_vs_revenue_chart
)

st.set_page_config(
    page_title="Corporate AI Adoption Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Corporate AI Adoption Analytics Dashboard")

df = load_data()

# Sidebar
st.sidebar.header("Filters")

industry = st.sidebar.multiselect(
    "Industry",
    df["industry"].unique(),
    default=df["industry"].unique()
)

country = st.sidebar.multiselect(
    "Country",
    df["country"].unique(),
    default=df["country"].unique()
)

filtered_df = df[
    (df["industry"].isin(industry)) &
    (df["country"].isin(country))
]

# KPIs
kpis = get_kpis(filtered_df)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Companies", f"{kpis['companies']:,}")
c2.metric("Avg AI Adoption", f"{kpis['adoption']:.2f}")
c3.metric("AI Investment", f"${kpis['investment']:,.0f}")
c4.metric("Revenue Impact", f"${kpis['revenue']:,.0f}")

st.divider()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        adoption_trend_chart(filtered_df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        industry_chart(industry_summary(filtered_df)),
        use_container_width=True
    )

col3, col4 = st.columns(2)

with col3:
    st.plotly_chart(
        country_chart(country_summary(filtered_df)),
        use_container_width=True
    )

with col4:
    st.plotly_chart(
        investment_vs_revenue_chart(filtered_df),
        use_container_width=True
    )

# Deep Insights
st.subheader("📈 AI Insights")

best_industry = (
    filtered_df.groupby("industry")["ai_adoption_level"]
    .mean()
    .idxmax()
)

best_country = (
    filtered_df.groupby("country")["revenue_impact"]
    .mean()
    .idxmax()
)

st.success(
    f"""
    • Highest AI adoption industry: **{best_industry}**

    • Highest revenue impact country: **{best_country}**

    • Average AI maturity score:
      **{filtered_df['ai_maturity_score'].mean():.2f}**

    • Average productivity gain:
      **{filtered_df['productivity_gain'].mean():.2%}**
    """
)

st.dataframe(filtered_df.head(100))
