import sqlite3
import pandas as pd
from database import get_connection

# query to return table
def execute_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# query to return single values safely
def execute_scalar(query):
    conn = get_connection()
    res = conn.execute(query).fetchone()
    conn.close()
    if res is not None and res[0] is not None:
        return res[0]
    return 0
