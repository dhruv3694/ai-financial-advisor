from numpy import select
import sqlite3
import pandas as pd

# Read CSV
df = pd.read_csv("sampleDataset.csv")

# Create/connect to SQLite database
conn = sqlite3.connect("fintech.db")

# Create SQL table from CSV
df.to_sql("transactions" , conn, if_exists="replace", index=False)

# print("CSV imported successfully!")

# query = """
# SELECT *
# FROM transactions
# LIMIT 5;
# """

# result = pd.read_sql(query, conn)

# print(result)

query = """
SELECT *
FROM transactions
WHERE "Customer Profile.risk_tolerance" = 'High';
"""

result = pd.read_sql(query, conn)

print(result)


print(df.columns.tolist())
conn.close()

