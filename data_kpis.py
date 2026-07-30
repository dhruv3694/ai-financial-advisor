from data_functions import execute_scalar,execute_query

def total_customers():
    query = """
    SELECT COUNT(*)
    FROM customer_dashboard;
    """
    execute_scalar(query)

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

