import plotly.express as px
import plotly.graph_objects as go
from data_kpis import *

def apply_layout(fig):
    """
    Applies common formatting to every chart.
    """

    fig.update_layout(

        template="plotly_white",

        title_x=0.5,

        height=500,
        hovermode="closest",

        font=dict(
            family="Arial",
            size=14
        ),

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),

        legend_title_text=""

    )

    fig.update_xaxes(showgrid=False)

    fig.update_yaxes(showgrid=True)

    return fig


# Customer Charts

def risk_distribution_chart(df):

    fig = px.bar(

        df,

        x="risk_tolerance",

        y="customers",

        title="Customer Risk Distribution",

        labels={

            "risk_tolerance":"Risk Category",

            "customers":"Number of Customers"

        }

    )

    return apply_layout(fig)


def occupation_distribution_chart(df):

    fig = px.bar(

        df,

        x="occupation",

        y="customers",

        title="Customer Occupation Distribution",

        labels={

            "occupation":"Occupation",

            "customers":"Customers"

        }

    )

    fig.update_xaxes(tickangle=-45)

    return apply_layout(fig)


def region_distribution_chart(df):

    fig = px.pie(

        df,

        names="region",

        values="customers",

        title="Customer Distribution by Region"

    )

    return apply_layout(fig)

def age_distribution_chart(df):

    fig = px.histogram(

        df,

        x="age",

        nbins=20,

        title="Customer Age Distribution"

    )

    return apply_layout(fig)

def income_distribution_chart(df):

    fig = px.histogram(

        df,

        x="annual_income",

        nbins=25,

        title="Customer Income Distribution",

        labels={

            "annual_income":"Annual Income"

        }

    )

    return apply_layout(fig)

# Account Charts

def balance_distribution_chart(df):

    fig = px.histogram(
        df,
        x="balance",
        nbins=30,
        title="Customer Balance Distribution",
        labels={
            "balance": "Account Balance"
        }
    )

    return apply_layout(fig)

def deposits_vs_withdrawals_chart(df):

    fig = px.bar(
        df,
        x="Metric",
        y="Amount",
        title="Deposits vs Withdrawals",
        text_auto=".2s"
    )

    return apply_layout(fig)

def account_type_distribution_chart(df):

    fig = px.pie(
        df,
        names="account_type",
        values="customers",
        title="Account Type Distribution"
    )

    return apply_layout(fig)

def investment_distribution_chart(df):

    fig = px.histogram(
        df,
        x="investments",
        nbins=25,
        title="Investment Distribution",
        labels={
            "investments": "Investment Amount"
        }
    )

    return apply_layout(fig)

def investment_distribution_chart(df):

    fig = px.histogram(
        df,
        x="investments",
        nbins=25,
        title="Investment Distribution",
        labels={
            "investments": "Investment Amount"
        }
    )

    return apply_layout(fig)


# Loan Analytics

def loan_status_chart(df):

    fig = px.pie(
        df,
        names="loan_status",
        values="count",
        title="Loan Application Status"
    )

    fig.update_traces(textposition="inside",
                      textinfo="percent+label")

    return apply_layout(fig)

def loan_amount_distribution_chart(df):

    fig = px.histogram(
        df,
        x="loan_amount",
        nbins=25,
        title="Loan Amount Distribution",
        labels={
            "loan_amount": "Loan Amount"
        }
    )

    return apply_layout(fig)

def interest_rate_distribution_chart(df):

    fig = px.histogram(
        df,
        x="interest_rate",
        nbins=20,
        title="Interest Rate Distribution",
        labels={
            "interest_rate": "Interest Rate (%)"
        }
    )

    return apply_layout(fig)

def loan_purpose_chart(df):

    fig = px.bar(
        df,
        x="loan_purpose",
        y="count",
        title="Loan Purpose Distribution",
        text_auto=True
    )

    fig.update_xaxes(tickangle=-30)

    return apply_layout(fig)

def average_loan_by_purpose_chart(df):

    fig = px.bar(
        df,
        x="loan_purpose",
        y="average_loan",
        title="Average Loan Amount by Purpose",
        text_auto=".2s"
    )

    return apply_layout(fig)

def interest_vs_loan_chart(df):

    fig = px.scatter(
        df,
        x="loan_amount",
        y="interest_rate",
        title="Loan Amount vs Interest Rate",
        labels={
            "loan_amount": "Loan Amount",
            "interest_rate": "Interest Rate (%)"
        }
    )

    return apply_layout(fig)


def approval_by_risk_chart(df):

    fig = px.bar(
        df,
        x="risk_tolerance",
        y="customers",
        color="loan_status",
        barmode="group",
        title="Loan Approval by Risk Category"
    )

    return apply_layout(fig)


# Transaction Charts

def transaction_trend_chart(df):

    fig = px.line(
        df,
        x="transaction_date",
        y="transactions",
        title="Transaction Trend Over Time",
        markers=True,
        labels={
            "transaction_date": "Date",
            "transactions": "Number of Transactions"
        }
    )

    return apply_layout(fig)


def deposits_withdrawals_trend_chart(df):

    fig = px.line(
        df,
        x="month",
        y=["deposits", "withdrawals"],
        title="Deposits vs Withdrawals Over Time",
        markers=True
    )

    return apply_layout(fig)


def repayment_trend_chart(df):

    fig = px.line(
        df,
        x="month",
        y="repayments",
        title="Loan Repayment Trend",
        markers=True
    )

    return apply_layout(fig)

def monthly_transaction_chart(df):

    fig = px.bar(
        df,
        x="month",
        y="transactions",
        title="Monthly Transaction Volume",
        text_auto=True
    )

    return apply_layout(fig)

def transaction_type_chart(df):

    fig = px.bar(
        df,
        x="transaction_type",
        y="count",
        title="Transaction Type Distribution",
        text_auto=True
    )

    return apply_layout(fig)

def top_transaction_customers_chart(df):

    fig = px.bar(
        df,
        x="customer_name",
        y="transactions",
        title="Top Customers by Number of Transactions",
        text_auto=True
    )

    fig.update_xaxes(tickangle=-45)

    return apply_layout(fig)

def repayment_boxplot(df):

    fig = px.box(
        df,
        y="repayments",
        title="Loan Repayment Distribution"
    )

    return apply_layout(fig)

def average_transaction_value_chart(df):

    fig = px.line(
        df,
        x="month",
        y="average_transaction",
        title="Average Transaction Value",
        markers=True
    )

    return apply_layout(fig)

