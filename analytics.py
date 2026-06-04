import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    return pd.read_csv("corporate_ai_adoption_dataset.csv")


def get_kpis(df):
    return {
        "companies": len(df),
        "adoption": df["ai_adoption_level"].mean(),
        "investment": df["ai_investment_usd"].sum(),
        "revenue": df["revenue_impact"].sum()
    }


def industry_summary(df):
    return (
        df.groupby("industry")
        .agg({
            "ai_adoption_level": "mean",
            "ai_investment_usd": "sum"
        })
        .reset_index()
    )


def country_summary(df):
    return (
        df.groupby("country")
        .agg({
            "revenue_impact": "sum"
        })
        .reset_index()
        .sort_values(
            "revenue_impact",
            ascending=False
        )
    )
