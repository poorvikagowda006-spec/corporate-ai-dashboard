import plotly.express as px


def adoption_trend_chart(df):

    yearly = (
        df.groupby("year")["ai_adoption_level"]
        .mean()
        .reset_index()
    )

    fig = px.line(
        yearly,
        x="year",
        y="ai_adoption_level",
        markers=True,
        title="AI Adoption Trend"
    )

    return fig


def industry_chart(df):

    fig = px.bar(
        df,
        x="industry",
        y="ai_adoption_level",
        title="Industry Adoption Level"
    )

    return fig


def country_chart(df):

    fig = px.bar(
        df.head(10),
        x="country",
        y="revenue_impact",
        title="Top Countries by Revenue Impact"
    )

    return fig


def investment_vs_revenue_chart(df):

    sample = df.sample(
        min(3000, len(df)),
        random_state=42
    )

    fig = px.scatter(
        sample,
        x="ai_investment_usd",
        y="revenue_impact",
        color="industry",
        title="Investment vs Revenue Impact"
    )

    return fig
