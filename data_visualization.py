import plotly.express as px
import plotly.graph_objects as go


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
    col = "risk_tolerance" if "risk_tolerance" in df.columns else df.columns[0]
    val = "customers" if "customers" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.bar(
        df,
        x=col,
        y=val,
        title="Customer Risk Distribution",
        labels={
            col: "Risk Category",
            val: "Number of Customers"
        }
    )
    return apply_layout(fig)


def occupation_distribution_chart(df):
    col = "occupation" if "occupation" in df.columns else df.columns[0]
    val = "customers" if "customers" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.bar(
        df,
        x=col,
        y=val,
        title="Customer Occupation Distribution",
        labels={
            col: "Occupation",
            val: "Customers"
        }
    )
    fig.update_xaxes(tickangle=-45)
    return apply_layout(fig)


def region_distribution_chart(df):
    col = "region" if "region" in df.columns else df.columns[0]
    val = "customers" if "customers" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.pie(
        df,
        names=col,
        values=val,
        title="Customer Distribution by Region"
    )
    return apply_layout(fig)


def age_distribution_chart(df):
    col = "age" if "age" in df.columns else df.columns[0]
    fig = px.histogram(
        df,
        x=col,
        nbins=20,
        title="Customer Age Distribution"
    )
    return apply_layout(fig)


def income_distribution_chart(df):
    col = "income_level" if "income_level" in df.columns else ("annual_income" if "annual_income" in df.columns else df.columns[0])
    fig = px.histogram(
        df,
        x=col,
        nbins=25,
        title="Customer Income Distribution",
        labels={
            col: "Income Level"
        }
    )
    return apply_layout(fig)


# Account Charts

def balance_distribution_chart(df):
    col = "balance" if "balance" in df.columns else df.columns[0]
    fig = px.histogram(
        df,
        x=col,
        nbins=30,
        title="Customer Balance Distribution",
        labels={
            col: "Account Balance"
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
    col = "account_type" if "account_type" in df.columns else df.columns[0]
    val = "customers" if "customers" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.pie(
        df,
        names=col,
        values=val,
        title="Account Type Distribution"
    )
    return apply_layout(fig)


def investment_distribution_chart(df):
    col = "investments" if "investments" in df.columns else df.columns[0]
    fig = px.histogram(
        df,
        x=col,
        nbins=25,
        title="Investment Distribution",
        labels={
            col: "Investment Amount"
        }
    )
    return apply_layout(fig)


# Loan Analytics

def loan_status_chart(df):
    col = "loan_status" if "loan_status" in df.columns else df.columns[0]
    val = "count" if "count" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.pie(
        df,
        names=col,
        values=val,
        title="Loan Application Status"
    )
    fig.update_traces(textposition="inside", textinfo="percent+label")
    return apply_layout(fig)


def loan_amount_distribution_chart(df):
    col = "loan_amount" if "loan_amount" in df.columns else df.columns[0]
    fig = px.histogram(
        df,
        x=col,
        nbins=25,
        title="Loan Amount Distribution",
        labels={
            col: "Loan Amount"
        }
    )
    return apply_layout(fig)


def interest_rate_distribution_chart(df):
    col = "interest_rate" if "interest_rate" in df.columns else df.columns[0]
    fig = px.histogram(
        df,
        x=col,
        nbins=20,
        title="Interest Rate Distribution",
        labels={
            col: "Interest Rate (%)"
        }
    )
    return apply_layout(fig)


def loan_purpose_chart(df):
    col = "loan_purpose" if "loan_purpose" in df.columns else df.columns[0]
    val = "count" if "count" in df.columns else (df.columns[1] if len(df.columns) > 1 else df.columns[0])
    fig = px.bar(
        df,
        x=col,
        y=val,
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
    col_x = "transaction_date" if "transaction_date" in df.columns else df.columns[0]
    col_y = "transactions" if "transactions" in df.columns else df.columns[1]
    fig = px.line(
        df,
        x=col_x,
        y=col_y,
        title="Transaction Trend Over Time",
        markers=True,
        labels={
            col_x: "Date",
            col_y: "Transactions"
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
    col_x = "month" if "month" in df.columns else df.columns[0]
    col_y = "repayments" if "repayments" in df.columns else df.columns[1]
    fig = px.line(
        df,
        x=col_x,
        y=col_y,
        title="Loan Repayment Trend",
        markers=True
    )
    return apply_layout(fig)


def monthly_transaction_chart(df):
    col_x = "month" if "month" in df.columns else df.columns[0]
    col_y = "transactions" if "transactions" in df.columns else df.columns[1]
    fig = px.bar(
        df,
        x=col_x,
        y=col_y,
        title="Monthly Transaction Volume",
        text_auto=True
    )
    return apply_layout(fig)


def transaction_type_chart(df):
    col_x = "transaction_type" if "transaction_type" in df.columns else df.columns[0]
    col_y = "count" if "count" in df.columns else df.columns[1]
    fig = px.bar(
        df,
        x=col_x,
        y=col_y,
        title="Transaction Type Distribution",
        text_auto=True
    )
    return apply_layout(fig)


def top_transaction_customers_chart(df):
    col_x = "customer_name" if "customer_name" in df.columns else ("customer_id" if "customer_id" in df.columns else df.columns[0])
    col_y = "transactions" if "transactions" in df.columns else df.columns[1]
    fig = px.bar(
        df,
        x=col_x,
        y=col_y,
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
    if "month" in df.columns:
        fig = px.line(
            df,
            x="month",
            y="average_transaction",
            title="Average Transaction Value",
            markers=True
        )
    else:
        col_x = "transaction_type" if "transaction_type" in df.columns else df.columns[0]
        col_y = "average_value" if "average_value" in df.columns else df.columns[1]
        fig = px.bar(
            df,
            x=col_x,
            y=col_y,
            title="Average Transaction Value by Type",
            text_auto=".2f"
        )
    return apply_layout(fig)


# Relationship Charts

def balance_vs_transactions_chart(df):
    fig = px.scatter(
        df,
        x="balance",
        y="transactions",
        title="Balance vs Number of Transactions",
        labels={
            "balance": "Account Balance",
            "transactions": "Transactions"
        },
        opacity=0.7
    )
    return apply_layout(fig)


def income_vs_investment_chart(df):
    col_x = "income_level" if "income_level" in df.columns else ("annual_income" if "annual_income" in df.columns else df.columns[0])
    col_y = "investments" if "investments" in df.columns else df.columns[1]
    fig = px.scatter(
        df,
        x=col_x,
        y=col_y,
        title="Income vs Investment",
        labels={
            col_x: "Income Level",
            col_y: "Investment Amount"
        },
        opacity=0.7
    )
    return apply_layout(fig)


def credit_score_vs_loan_chart(df):
    fig = px.scatter(
        df,
        x="credit_score",
        y="loan_amount",
        title="Credit Score vs Loan Amount",
        labels={
            "credit_score": "Credit Score",
            "loan_amount": "Loan Amount"
        }
    )
    return apply_layout(fig)


def risk_vs_investment_chart(df):
    col_x = "risk_tolerance" if "risk_tolerance" in df.columns else df.columns[0]
    col_y = "investments" if "investments" in df.columns else df.columns[1]
    fig = px.box(
        df,
        x=col_x,
        y=col_y,
        title="Investment Distribution by Risk Category"
    )
    return apply_layout(fig)


def customer_segmentation_chart(df):
    col_x = "income_level" if "income_level" in df.columns else ("annual_income" if "annual_income" in df.columns else df.columns[0])
    fig = px.scatter(
        df,
        x=col_x,
        y="balance",
        color="risk_tolerance" if "risk_tolerance" in df.columns else None,
        title="Customer Segmentation",
        labels={
            col_x: "Income Level",
            "balance": "Account Balance"
        },
        opacity=0.7
    )
    return apply_layout(fig)


def occupation_balance_chart(df):
    fig = px.bar(
        df,
        x="occupation",
        y="average_balance",
        title="Average Balance by Occupation",
        text_auto=".2s"
    )
    fig.update_xaxes(tickangle=-45)
    return apply_layout(fig)
