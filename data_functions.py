import sqlite3
import pandas as pd
from database import get_connection

# query to return table
def execute_query(query):
    conn = get_connection()

    df = pd.read_sql(query, conn)

    conn.close()

    return df

    
# query to return single values
def execute_scalar(query):
    conn = get_connection()

    value = conn.execute(query).fetchone()[0]

    conn.close()

    return value

