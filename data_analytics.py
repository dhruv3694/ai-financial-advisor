from data_functions import execute_scalar,execute_query
import pandas as pd

def customer_dashboard():

    query = """
    SELECT *
    FROM customer_dashboard;
    """

    return execute_query(query)


def total_customers():
    query = """
    SELECT COUNT(*)
    FROM customer_dashboard;
    """
    return execute_scalar(query)

def average_age():

    query = """
    SELECT AVG(age)
    FROM customer_dashboard;
    """

    return round(execute_scalar(query),2)

def average_balance():

    query = """
    SELECT AVG(balance)
    FROM customer_dashboard;
    """

    return round(execute_scalar(query),2)

def total_deposits():

    query = """
    SELECT SUM(deposits)
    FROM customer_dashboard;
    """

    return execute_scalar(query)



# Risk Distribution

def risk_distribution():

    query = """

    SELECT

    risk_tolerance,

    COUNT(*) AS customers

    FROM customer_dashboard

    GROUP BY risk_tolerance;

    """

    return execute_query(query)

# Occupation Distribution

def occupation_distribution():

    query = """

    SELECT

    occupation,

    COUNT(*) AS customers

    FROM customer_dashboard

    GROUP BY occupation;

    """

    return execute_query(query)

# High Risk Customers

def high_risk_customers():

    query = """

    SELECT *

    FROM customer_dashboard

    WHERE risk_tolerance='High';

    """

    return execute_query(query)

# Approved Loans

def approved_loans():

    query = """

    SELECT *

    FROM customer_dashboard

    WHERE loan_status='Approved';

    """

    return execute_query(query)

# Premium Customers

def customer_segments():

    query = """

    SELECT

    customer_id,

    balance,

    CASE

        WHEN balance >= 100000 THEN 'Premium'

        WHEN balance >= 50000 THEN 'Gold'

        ELSE 'Regular'

    END AS customer_segment

    FROM customer_dashboard;

    """

    return execute_query(query)


# ✅ NEW: Total Accounts

def total_accounts():
    """Returns total number of accounts."""
    query = "SELECT COUNT(*) FROM account_dashboard;"
    return execute_scalar(query)


# ✅ NEW: Total Loans

def total_loans():
    """Returns total number of loans."""
    query = "SELECT COUNT(*) FROM loan_dashboard;"
    return execute_scalar(query)


# ✅ NEW: Total Transactions

def total_transactions():
    """Returns total number of transactions."""
    query = "SELECT COUNT(*) FROM transaction_dashboard;"
    return execute_scalar(query)


# ✅ NEW: Average Monthly Income

def average_monthly_income():
    """Returns average monthly income of customers."""
    query = "SELECT AVG(monthly_income) FROM customer_dashboard;"
    return round(execute_scalar(query), 2)


# ✅ NEW: Active Loans

def active_loans():
    """Returns count of active loans."""
    query = "SELECT COUNT(*) FROM loan_dashboard WHERE loan_status='Approved';"
    return execute_scalar(query)


# ✅ NEW: Average Loan Amount

def average_loan_amount():
    """Returns average loan amount."""
    query = "SELECT AVG(loan_amount) FROM loan_dashboard;"
    return round(execute_scalar(query), 2)


# ✅ NEW: Premium Customers (Balance >= 100k)

def premium_customers():
    """Returns count of premium customers."""
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE balance >= 100000;"
    return execute_scalar(query)


# ✅ NEW: High Balance Customers (Balance >= 50k)

def high_balance_customers():
    """Returns count of customers with >= 50k balance."""
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE balance >= 50000;"
    return execute_scalar(query)


# ✅ NEW: Total Loan Portfolio

def total_loan_portfolio():
    """Returns total loan portfolio amount."""
    query = "SELECT SUM(loan_amount) FROM loan_dashboard WHERE loan_status='Approved';"
    return execute_scalar(query)


# ✅ NEW: Account Types Count

def account_type_counts():
    """Returns count of each account type."""
    query = """
    SELECT
        account_type,
        COUNT(*) AS count
    FROM account_dashboard
    GROUP BY account_type;
    """
    return execute_query(query)


# ✅ NEW: Loan Status Distribution

def loan_status_distribution():
    """Returns distribution of loan statuses."""
    query = """
    SELECT
        loan_status,
        COUNT(*) AS count
    FROM loan_dashboard
    GROUP BY loan_status;
    """
    return execute_query(query)


# ✅ NEW: Risk Tolerance Distribution

def risk_tolerance_distribution():
    """Returns distribution of risk tolerances."""
    query = """
    SELECT
        risk_tolerance,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY risk_tolerance;
    """
    return execute_query(query)


# ✅ NEW: Customers per Region

def customers_per_region():
    """Returns number of customers per region."""
    query = """
    SELECT
        region,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY region;
    """
    return execute_query(query)


# ✅ NEW: Top Occupations

def top_occupations(limit=5):
    """Returns top occupations."""
    query = f"""
    SELECT
        occupation,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY occupation
    ORDER BY count DESC
    LIMIT {limit};
    """
    return execute_query(query)
    
def total_approved_loans():

    query = """
    SELECT COUNT(*)
    FROM customer_dashboard
    WHERE loan_status='Approved';
    """

    return execute_scalar(query)

def total_high_risk_customers():

    query = """
    SELECT COUNT(*)
    FROM customer_dashboard
    WHERE risk_tolerance='High';
    """

    return execute_scalar(query)

    

def total_approved_loans(df):
    query = """
    SELECT COUNT(*)
    FROM customer_dashboard
    WHERE loan_status='Approved';
    """
    return execute_scalar(query)

def total_high_risk_customers(df):
    query = """
    SELECT COUNT(*)
    FROM customer_dashboard
    WHERE risk_tolerance='High';
    """
    return execute_scalar(query)

def age_distribution():

    query = """
    SELECT age
    FROM customer_dashboard;
    """

    return execute_query(query)

def region_distribution():

    query = """

    SELECT
        region,
        COUNT(*) AS customers
    FROM customer_dashboard
    GROUP BY region;

    """

    return execute_query(query)

def balance_distribution():

    query = """
    SELECT balance
    FROM customer_dashboard;
    """

    return execute_query(query)

def account_type_distribution():

    query = """
    SELECT
        account_type,
        COUNT(*) AS customers
    FROM customer_dashboard
    GROUP BY account_type;
    """

    return execute_query(query)

def investment_distribution():

    query = """
    SELECT investments
    FROM customer_dashboard;
    """

    return execute_query(query)

def deposits_vs_withdrawals():

    query = """
    SELECT
        SUM(deposits) AS deposits,
        SUM(withdrawals) AS withdrawals
    FROM customer_dashboard;
    """

    df = execute_query(query)

    return pd.DataFrame({
        "Metric": ["Deposits", "Withdrawals"],
        "Amount": [
            df.loc[0, "deposits"],
            df.loc[0, "withdrawals"]
        ]
    })

def loan_status_distribution():

    query = """
    SELECT
        loan_status,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY loan_status;
    """

    return execute_query(query)

def loan_purpose_distribution():

    query = """
    SELECT
        loan_purpose,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY loan_purpose;
    """

    return execute_query(query)

def interest_rate_distribution():

    query = """
    SELECT interest_rate
    FROM customer_dashboard;
    """

    return execute_query(query)

def loan_amount_distribution():

    query = """
    SELECT loan_amount
    FROM customer_dashboard;
    """

    return execute_query(query)

def approval_by_risk():

    query = """
    SELECT
        risk_tolerance,
        loan_status,
        COUNT(*) AS customers
    FROM customer_dashboard
    GROUP BY
        risk_tolerance,
        loan_status;
    """

    return execute_query(query)

def interest_vs_loan():

    query = """
    SELECT
        loan_amount,
        interest_rate
    FROM customer_dashboard;
    """

    return execute_query(query)

def transaction_trend():

    query = """
    SELECT
        transaction_date,
        SUM(transaction_amount) AS total_transaction
    FROM customer_dashboard
    GROUP BY transaction_date
    ORDER BY transaction_date;
    """

    return execute_query(query)

def monthly_transactions():

    query = """
    SELECT
        strftime('%Y-%m', transaction_date) AS month,
        SUM(transaction_amount) AS total_transaction
    FROM customer_dashboard
    GROUP BY month
    ORDER BY month;
    """

    return execute_query(query)

def transaction_type_distribution():

    query = """
    SELECT
        transaction_type,
        COUNT(*) AS count
    FROM customer_dashboard
    GROUP BY transaction_type;
    """

    return execute_query(query)

def average_transaction_value():

    query = """
    SELECT
        transaction_type,
        AVG(transaction_amount) AS average_value
    FROM customer_dashboard
    GROUP BY transaction_type;
    """

    return execute_query(query)

def repayment_trend():

    query = """
    SELECT
        transaction_date,
        SUM(loan_repayment) AS repayment
    FROM customer_dashboard
    GROUP BY transaction_date
    ORDER BY transaction_date;
    """

    return execute_query(query)

def top_transaction_customers():

    query = """
    SELECT
        customer_id,
        SUM(transaction_amount) AS total_transaction
    FROM customer_dashboard
    GROUP BY customer_id
    ORDER BY total_transaction DESC
    LIMIT 10;
    """

    return execute_query(query)

def income_vs_investment():

    query = """
    SELECT
        income_level,
        investments
    FROM customer_dashboard;
    """

    return execute_query(query)

def customer_segmentation():

    query = """
    SELECT
        income_level,
        balance,
        risk_tolerance
    FROM customer_dashboard;
    """

    return execute_query(query)

def occupation_balance():

    query = """
    SELECT
        occupation,
        AVG(balance) AS average_balance
    FROM customer_dashboard
    GROUP BY occupation;
    """

    return execute_query(query)

def risk_vs_investment():

    query = """
    SELECT
        risk_tolerance,
        investments
    FROM customer_dashboard;
    """

    return execute_query(query)

