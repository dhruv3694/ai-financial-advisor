import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("fintech.db")


def load_csv():
    conn = get_connection()

    df = pd.read_csv("sampleDataset.csv")

    df.to_sql(
        "transactions",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


if __name__ == "__main__":
    load_csv()