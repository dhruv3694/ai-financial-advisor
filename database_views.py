import sqlite3
from database import get_connection

conn=get_connection()
cur=conn.cursor()

# customer dashboard

cur.executescript(
    """
DROP VIEW IF EXISTS customer_dashboard;

CREATE VIEW customer_dashboard AS

SELECT

cp.customer_id,

cp.age,
cp.occupation,
cp.risk_tolerance,
cp.investment_goals,
cp.education_level,
cp.marital_status,
cp.dependents,
cp.region,
cp.financial_history,
cp.sector,
cp.income_level,
cp.employment_history,

aa.account_type,
aa.balance,
aa.deposits,
aa.withdrawals,
aa.transfers,
aa.international_transfers,
aa.investments,
aa.transaction_threshold,

la.loan_amount,
la.loan_purpose,
la.loan_term,
la.interest_rate,
la.loan_status,

ts.transactions,
ts.repayments,
ts.dates

FROM Customer_Profile cp

LEFT JOIN Account_Activity aa
ON cp.customer_id=aa.customer_id

LEFT JOIN Loan_Applications la
ON cp.customer_id=la.customer_id

LEFT JOIN Time_Series ts
ON cp.customer_id=ts.customer_id;

"""
)

# loan dashboard view

cur.executescript(
    """
    DROP VIEW IF EXISTS loan_dashboard;

CREATE VIEW loan_dashboard AS

SELECT

cp.customer_id,
cp.age,
cp.income_level,
cp.risk_tolerance,

la.loan_amount,
la.loan_purpose,
la.loan_term,
la.interest_rate,
la.loan_status

FROM Customer_Profile cp

LEFT JOIN Loan_Applications la

ON cp.customer_id=la.customer_id;"""
)





# risk dashboard view

cur.executescript(
"""
DROP VIEW IF EXISTS risk_dashboard;

CREATE VIEW risk_dashboard AS

SELECT

cp.customer_id,

cp.age,

cp.income_level,

cp.risk_tolerance,

aa.balance,

aa.deposits,

aa.withdrawals,

aa.investments,

la.loan_amount,

la.interest_rate

FROM Customer_Profile cp

LEFT JOIN Account_Activity aa

ON cp.customer_id=aa.customer_id

LEFT JOIN Loan_Applications la

ON cp.customer_id=la.customer_id;
"""
)



# Investment Dashboard view

cur.executescript(
"""
DROP VIEW IF EXISTS investment_dashboard;

CREATE VIEW investment_dashboard AS

SELECT

cp.customer_id,

cp.age,

cp.investment_goals,

cp.risk_tolerance,

aa.investments,

aa.balance

FROM Customer_Profile cp

LEFT JOIN Account_Activity aa

ON cp.customer_id=aa.customer_id;

"""
)

# Transaction Dashboard

cur.executescript(
"""   DROP VIEW IF EXISTS transaction_dashboard;

CREATE VIEW transaction_dashboard AS

SELECT

cp.customer_id,

aa.balance,

ts.transactions,

ts.repayments,

ts.dates

FROM Customer_Profile cp

LEFT JOIN Account_Activity aa

ON cp.customer_id=aa.customer_id

LEFT JOIN Time_Series ts

ON cp.customer_id=ts.customer_id;"""
)

conn.commit()
conn.close()
