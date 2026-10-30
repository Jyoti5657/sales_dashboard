import streamlit as st
import pandas as pd
import plotly.express as px

LAKH = 100_000

# st.set_page_config(
#     page_title="ZSD Sales Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# Green-and-white dashboard styling; Plotly chart colors are unchanged.
st.markdown(
    """
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #16834a; }
    [data-testid="stSidebar"] * { color: #ffffff; }
    [data-testid="stSidebar"] button { border-color: #ffffff; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load data
df = pd.read_excel("zsd_salesreg2.xlsx")
df.columns = df.columns.str.strip()
df["Invoice Date"] = pd.to_datetime(df["Invoice Date"], errors="coerce")
df["_Invoice Month"] = df["Invoice Date"].dt.strftime("%Y-%m")


def show_chart_and_drilldown(fig, chart_data, label_col, filter_col, key):
    """Show a chart and the source rows for any selected chart points."""
    event = st.plotly_chart(
        fig,
        use_container_width=True,
        key=key,
        on_select="rerun",
        selection_mode="points",
    )

    points = event.selection.points
    indices = [
        point["point_index"]
        for point in points
        if point.get("point_index") is not None
    ]

    if indices:
        labels = chart_data.iloc[indices][label_col].dropna().unique()
        rows = df[df[filter_col].isin(labels)]

        st.subheader("Selected data rows")
        st.dataframe(rows, use_container_width=True, hide_index=True)


st.sidebar.title("📊 Dashboard Menu")
page = st.sidebar.radio(
    "Select Dashboard",
    [
        "Dashboard",
        "State Analysis",
        "Country Analysis",
        "Product Analysis",
        "Customer Analysis",
        "Sales Trend",
        "MIS Analysis",
    ],
)

if page == "Dashboard":
    st.title("📊 Sales Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Sales (₹ Lakhs)", f"{df['Invoice Value'].sum() / LAKH:,.2f}")
    col2.metric("Customers", df["Sold to Party Name"].nunique())
    col3.metric("States", df["State"].nunique())
    col4.metric("Products", df["PRODUCT TYPE"].nunique())

    state_sales = (
        df.groupby("State", as_index=False)["Invoice Value"]
        .sum()
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    state_sales["Sales (₹ Lakhs)"] /= LAKH

    country_sales = (
        df.groupby("Final Country", as_index=False)["Invoice Value"]
        .sum()
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    country_sales["Sales (₹ Lakhs)"] /= LAKH

    col_a, col_b = st.columns(2)

    with col_a:
        fig = px.pie(
            state_sales,
            names="State",
            values="Sales (₹ Lakhs)",
            hole=0.5,
            title="State Wise Sales (₹ Lakhs)",
        )
        show_chart_and_drilldown(
            fig, state_sales, "State", "State", "dashboard_state"
        )

    with col_b:
        fig = px.bar(
            country_sales,
            x="Final Country",
            y="Sales (₹ Lakhs)",
            title="Country Wise Sales (₹ Lakhs)",
        )
        show_chart_and_drilldown(
            fig, country_sales, "Final Country", "Final Country", "dashboard_country"
        )

elif page == "State Analysis":
    state_sales = (
        df.groupby("State", as_index=False)["Invoice Value"]
        .sum()
        .sort_values("Invoice Value", ascending=False)
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    state_sales["Sales (₹ Lakhs)"] /= LAKH

    fig = px.bar(
        state_sales,
        x="State",
        y="Sales (₹ Lakhs)",
        color="Sales (₹ Lakhs)",
        title="State Wise Sales (₹ Lakhs)",
    )
    show_chart_and_drilldown(fig, state_sales, "State", "State", "state_analysis")

elif page == "Country Analysis":
    country_sales = (
        df.groupby("Final Country", as_index=False)["Invoice Value"]
        .sum()
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    country_sales["Sales (₹ Lakhs)"] /= LAKH

    fig = px.pie(
        country_sales,
        names="Final Country",
        values="Sales (₹ Lakhs)",
        hole=0.5,
        title="Country Wise Sales (₹ Lakhs)",
    )
    show_chart_and_drilldown(
        fig, country_sales, "Final Country", "Final Country", "country_analysis"
    )

elif page == "Product Analysis":
    product_sales = (
        df.groupby("PRODUCT TYPE", as_index=False)["Invoice Value"]
        .sum()
        .sort_values("Invoice Value", ascending=False)
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    product_sales["Sales (₹ Lakhs)"] /= LAKH

    fig = px.bar(
        product_sales,
        x="PRODUCT TYPE",
        y="Sales (₹ Lakhs)",
        color="Sales (₹ Lakhs)",
        title="Product Sales (₹ Lakhs)",
    )
    show_chart_and_drilldown(
        fig, product_sales, "PRODUCT TYPE", "PRODUCT TYPE", "product_analysis"
    )

elif page == "Customer Analysis":
    customer_sales = (
        df.groupby("Sold to Party Name", as_index=False)["Invoice Value"]
        .sum()
        .sort_values("Invoice Value", ascending=False)
        .head(10)
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    customer_sales["Sales (₹ Lakhs)"] /= LAKH

    fig = px.bar(
        customer_sales,
        x="Sold to Party Name",
        y="Sales (₹ Lakhs)",
        color="Sales (₹ Lakhs)",
        title="Top 10 Customers (₹ Lakhs)",
    )
    show_chart_and_drilldown(
        fig,
        customer_sales,
        "Sold to Party Name",
        "Sold to Party Name",
        "customer_analysis",
    )

elif page == "Sales Trend":
    trend = (
        df.dropna(subset=["_Invoice Month"])
        .groupby("_Invoice Month", as_index=False)["Invoice Value"]
        .sum()
        .rename(columns={"_Invoice Month": "Invoice Month",
                         "Invoice Value": "Sales (₹ Lakhs)"})
    )
    trend["Sales (₹ Lakhs)"] /= LAKH

    fig = px.line(
        trend,
        x="Invoice Month",
        y="Sales (₹ Lakhs)",
        markers=True,
        title="Monthly Sales Trend (₹ Lakhs)",
    )
    show_chart_and_drilldown(
        fig, trend, "Invoice Month", "_Invoice Month", "sales_trend"
    )

elif page == "MIS Analysis":
    mis_sales = (
        df.groupby("MIS Group", as_index=False)["Invoice Value"]
        .sum()
        .sort_values("Invoice Value", ascending=False)
        .head(15)
        .rename(columns={"Invoice Value": "Sales (₹ Lakhs)"})
    )
    mis_sales["Sales (₹ Lakhs)"] /= LAKH

    fig = px.bar(
        mis_sales,
        x="MIS Group",
        y="Sales (₹ Lakhs)",
        color="Sales (₹ Lakhs)",
        title="MIS Group Analysis (₹ Lakhs)",
    )
    show_chart_and_drilldown(
        fig, mis_sales, "MIS Group", "MIS Group", "mis_analysis"
    )