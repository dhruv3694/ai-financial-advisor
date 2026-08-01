import streamlit as st

# ==========================================================
# Analytics & Visualization Layer
# ==========================================================

from data_analytics import (
    total_customers,
    average_age,
    average_balance,
    total_deposits,
    approved_loans,
    total_high_risk_customers,
    risk_distribution,
    occupation_distribution,
    region_distribution,
    age_distribution,
    balance_distribution,
    account_type_distribution,
    investment_distribution,
    deposits_vs_withdrawals,
    loan_status_distribution,
    loan_purpose_distribution,
    interest_rate_distribution,
    loan_amount_distribution,
    approval_by_risk,
    interest_vs_loan,
    transaction_trend,
    monthly_transactions,
    transaction_type_distribution,
    average_transaction_value,
    repayment_trend,
    top_transaction_customers,
    income_vs_investment,
    customer_segmentation,
    risk_vs_investment,
    occupation_balance,
)

from data_visualization import (
    risk_distribution_chart,
    occupation_distribution_chart,
    region_distribution_chart,
    age_distribution_chart,
    balance_distribution_chart,
    account_type_distribution_chart,
    investment_distribution_chart,
    deposits_vs_withdrawals_chart,
    loan_status_chart,
    loan_purpose_chart,
    interest_rate_distribution_chart,
    loan_amount_distribution_chart,
    approval_by_risk_chart,
    interest_vs_loan_chart,
    transaction_trend_chart,
    monthly_transaction_chart,
    transaction_type_chart,
    average_transaction_value_chart,
    repayment_trend_chart,
    top_transaction_customers_chart,
    income_vs_investment_chart,
    customer_segmentation_chart,
    risk_vs_investment_chart,
    occupation_balance_chart,
)

# ==========================================================
# Dashboard Components
# ==========================================================

from dashboard_components import (
    create_metric_card,
    create_section_header,
    create_chart_container,
    create_divider,
    create_info_box,
)

# ==========================================================
# Main Dashboard
# ==========================================================

def render_dashboard(df):
    """
    Main dashboard renderer.

    Parameters
    ----------
    df : pandas.DataFrame
        Filtered dataframe received from sidebar.py
    """

    # ------------------------------------------------------
    # Dashboard Title
    # ------------------------------------------------------

    create_section_header("🏦 FinTech Analytics Dashboard")

    st.caption(
        "Interactive dashboard for customer, account, loan and transaction analytics."
    )

    # ------------------------------------------------------
    # Empty Data Handling
    # ------------------------------------------------------

    if df is None or df.empty:
        st.warning(
            "No records found for the selected filters."
        )
        return

    # ======================================================
    # KPI SECTION
    # ======================================================

    render_kpi_section(df)

    create_divider()

    # ======================================================
    # CUSTOMER ANALYTICS
    # ======================================================

    render_customer_section(df)

    create_divider()

    # ======================================================
    # ACCOUNT ANALYTICS
    # ======================================================

    render_account_section(df)

    create_divider()

    # ======================================================
    # LOAN ANALYTICS
    # ======================================================

    render_loan_section(df)

    create_divider()

    # ======================================================
    # TRANSACTION ANALYTICS
    # ======================================================

    render_transaction_section(df)

    create_divider()

    # ======================================================
    # RELATIONSHIP ANALYTICS
    # ======================================================

    render_relationship_section(df)


# ==========================================================
# KPI SECTION
# ==========================================================

def render_kpi_section(df):

    create_section_header("📊 Key Performance Indicators")

    st.caption(
        "Quick overview of the most important business metrics."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        create_metric_card(
            title="Total Customers",
            value=f"{total_customers(df):,}"
        )

    with col2:
        create_metric_card(
            title="Average Age",
            value=f"{average_age(df):.1f} Years"
        )

    with col3:
        create_metric_card(
            title="Average Balance",
            value=f"${average_balance(df):,.2f}"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        create_metric_card(
            title="Total Deposits",
            value=f"${total_deposits(df):,.2f}"
        )

    with col5:
        create_metric_card(
            title="Approved Loans",
            value=f"{len(approved_loans(df)):,}"
        )

    with col6:
        create_metric_card(
            title="High Risk Customers",
            value=f"{total_high_risk_customers(df):,}"
        )


# ==========================================================
# CUSTOMER ANALYTICS
# ==========================================================

def render_customer_section(df):

    create_section_header("👥 Customer Analytics")

    st.caption(
        "Understand customer demographics, occupation and risk profile."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container():
            risk_df = risk_distribution(df)
            fig = risk_distribution_chart(risk_df)
            create_chart_container(fig)

    with col2:
        with st.container():
            occupation_df = occupation_distribution(df)
            fig = occupation_distribution_chart(occupation_df)
            create_chart_container(fig)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        with st.container():
            region_df = region_distribution(df)
            fig = region_distribution_chart(region_df)
            create_chart_container(fig)

    with col4:
        with st.container():
            age_df = age_distribution(df)
            fig = age_distribution_chart(age_df)
            create_chart_container(fig)


# ==========================================================
# ACCOUNT ANALYTICS
# ==========================================================

def render_account_section(df):

    create_section_header("🏦 Account Analytics")

    st.caption(
        "Analyze customer accounts, balances and investment patterns."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container():
            balance_df = balance_distribution(df)
            fig = balance_distribution_chart(balance_df)
            create_chart_container(fig)

    with col2:
        with st.container():
            account_df = account_type_distribution(df)
            fig = account_type_distribution_chart(account_df)
            create_chart_container(fig)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        with st.container():
            investment_df = investment_distribution(df)
            fig = investment_distribution_chart(investment_df)
            create_chart_container(fig)

    with col4:
        with st.container():
            deposits_df = deposits_vs_withdrawals(df)
            fig = deposits_vs_withdrawals_chart(deposits_df)
            create_chart_container(fig)


# ==========================================================
# LOAN ANALYTICS
# ==========================================================

def render_loan_section(df):

    create_section_header("🏦 Loan Analytics")

    st.caption(
        "Analyze loan approvals, interest rates and lending behaviour."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        fig = loan_status_chart(loan_status_distribution(df))
        create_chart_container(fig)

    with col2:
        fig = loan_purpose_chart(loan_purpose_distribution(df))
        create_chart_container(fig)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        fig = interest_rate_distribution_chart(interest_rate_distribution(df))
        create_chart_container(fig)

    with col4:
        fig = loan_amount_distribution_chart(loan_amount_distribution(df))
        create_chart_container(fig)

    col5, col6 = st.columns(2, gap="large")

    with col5:
        fig = approval_by_risk_chart(approval_by_risk(df))
        create_chart_container(fig)

    with col6:
        fig = interest_vs_loan_chart(interest_vs_loan(df))
        create_chart_container(fig)


# ==========================================================
# TRANSACTION ANALYTICS
# ==========================================================

def render_transaction_section(df):

    create_section_header("💳 Transaction Analytics")

    st.caption(
        "Monitor transaction activity, repayment behaviour and customer spending."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        fig = transaction_trend_chart(transaction_trend(df))
        create_chart_container(fig)

    with col2:
        fig = monthly_transaction_chart(monthly_transactions(df))
        create_chart_container(fig)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        fig = transaction_type_chart(transaction_type_distribution(df))
        create_chart_container(fig)

    with col4:
        fig = average_transaction_value_chart(average_transaction_value(df))
        create_chart_container(fig)

    col5, col6 = st.columns(2, gap="large")

    with col5:
        fig = repayment_trend_chart(repayment_trend(df))
        create_chart_container(fig)

    with col6:
        fig = top_transaction_customers_chart(top_transaction_customers(df))
        create_chart_container(fig)


# ==========================================================
# RELATIONSHIP ANALYTICS
# ==========================================================

def render_relationship_section(df):

    create_section_header("📈 Relationship Analytics")

    st.caption(
        "Discover relationships between customer income, investments and financial behaviour."
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        fig = income_vs_investment_chart(income_vs_investment(df))
        create_chart_container(fig)

    with col2:
        fig = customer_segmentation_chart(customer_segmentation(df))
        create_chart_container(fig)

    col3, col4 = st.columns(2, gap="large")

    with col3:
        fig = risk_vs_investment_chart(risk_vs_investment(df))
        create_chart_container(fig)

    with col4:
        fig = occupation_balance_chart(occupation_balance(df))
        create_chart_container(fig)
