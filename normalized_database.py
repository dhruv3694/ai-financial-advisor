# pyrefly: ignore [missing-import]
import sqlite3 
import pandas as pd 
from database import get_connection

conn=get_connection()
# all actions or queries will be done on database we made

cur = conn.cursor()

# drop the tables if existed to create new one

cur.executescript("""

DROP TABLE IF EXISTS Customer_Profile;
DROP TABLE IF EXISTS Account_Activity;
DROP TABLE IF EXISTS Loan_Applications;
DROP TABLE IF EXISTS Time_Series;

""")

# create tables for normalization

cur.execute("""

CREATE TABLE Customer_Profile(

customer_id TEXT PRIMARY KEY,

age INTEGER,

occupation TEXT,

risk_tolerance TEXT,

investment_goals TEXT,

education_level TEXT,

marital_status TEXT,

dependents INTEGER,

region TEXT,

financial_history TEXT,

sector TEXT,

income_level TEXT,

employment_history TEXT,

address TEXT

);

""")

cur.execute("""

INSERT INTO Customer_Profile

SELECT DISTINCT

"Customer Profile.customer_id",

"Customer Profile.age",

"Customer Profile.occupation",

"Customer Profile.risk_tolerance",

"Customer Profile.investment_goals",

"Customer Profile.education_level",

"Customer Profile.marital_status",

"Customer Profile.dependents",

"Customer Profile.region",

"Customer Profile.financial_history",

"Customer Profile.sector",

"Customer Profile.income_level",

"Customer Profile.employment_history",

"Customer Profile.address"

FROM transactions;

""")


cur.execute("""

CREATE TABLE Account_Activity(

account_id TEXT PRIMARY KEY,

customer_id INTEGER,

balance REAL,

deposits REAL,

withdrawals REAL,

transfers REAL,

international_transfers REAL,

investments REAL,

account_type TEXT,

transaction_threshold REAL,

FOREIGN KEY(customer_id)

REFERENCES Customer_Profile(customer_id)

);

""")

cur.execute("""

INSERT INTO Account_Activity

SELECT

"Account Activity.account_id",

"Account Activity.customer_id",

"Account Activity.balance",

"Account Activity.deposits",

"Account Activity.withdrawals",

"Account Activity.transfers",

"Account Activity.international_transfers",

"Account Activity.investments",

"Account Activity.account_type",

"Account Activity.transaction_threshold"

FROM transactions;

""")

cur.execute("""
CREATE TABLE Loan_Applications(

    loan_id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_id TEXT,

    loan_amount REAL,

    loan_purpose TEXT,

    employment_status TEXT,

    loan_term INTEGER,

    interest_rate REAL,

    loan_status TEXT,

    FOREIGN KEY(customer_id)
    REFERENCES Customer_Profile(customer_id)

);
""")

cur.execute("""
INSERT INTO Loan_Applications(

customer_id,
loan_amount,
loan_purpose,
employment_status,
loan_term,
interest_rate,
loan_status

)

SELECT

"Customer Profile.customer_id",

"Loan Application Summary.loan_amount",

"Loan Application Summary.loan_purpose",

"Loan Application Summary.employment_status",

"Loan Application Summary.loan_term",

"Loan Application Summary.interest_rate",

"Loan Application Summary.loan_status"

FROM transactions;
""")

cur.execute("""
CREATE TABLE Time_Series(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_id TEXT,

    dates TEXT,

    transactions INTEGER,

    repayments REAL,

    FOREIGN KEY(customer_id)
    REFERENCES Customer_Profile(customer_id)

);
""")

cur.execute("""
INSERT INTO Time_Series(

customer_id,
dates,
transactions,
repayments

)

SELECT

"Customer Profile.customer_id",

"Time Series Data.dates",

"Time Series Data.transactions",

"Time Series Data.repayments"

FROM transactions;
""")




























conn.commit()

conn.close()

# # to test if tables are formed or not

# print(pd.read_sql("SELECT COUNT(*) FROM Customer_Profile", conn))

# print(pd.read_sql("SELECT COUNT(*) FROM Account_Activity", conn))

# print(pd.read_sql("SELECT COUNT(*) FROM Loan_Applications", conn))

# print(pd.read_sql("SELECT COUNT(*) FROM Time_Series", conn))





# query='''SELECT *
# FROM transactions
# WHERE "Customer Profile.risk_tolerance"='High'
# limit 5;'''

# df=pd.read_sql(query,conn)
# print(df)




