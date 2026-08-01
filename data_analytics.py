import re
import pandas as pd
from data_functions import execute_scalar, execute_query

DATE_PAT = re.compile(r'(\d{4}),\s*(\d{1,2}),\s*(\d{1,2})')
NUM_PAT = re.compile(r'[-+]?\d*\.\d+|\d+')


def customer_dashboard():
    query = """
    SELECT *
    FROM customer_dashboard;
    """
    df = execute_query(query)
    
    # Clean numeric columns
    numeric_cols = [
        "age", "balance", "deposits", "withdrawals", "transfers",
        "international_transfers", "investments", "transaction_threshold",
        "loan_amount", "loan_term", "interest_rate", "income_level"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            
    return df


def _get_active_df(df=None):
    if df is not None:
        return df
    return customer_dashboard()


def total_customers(df=None):
    if df is not None:
        return len(df)
    query = "SELECT COUNT(*) FROM customer_dashboard;"
    return execute_scalar(query)


def average_age(df=None):
    if df is not None:
        return round(float(df["age"].mean()), 2) if not df.empty and "age" in df else 0.0
    query = "SELECT AVG(age) FROM customer_dashboard;"
    val = execute_scalar(query)
    return round(float(val), 2) if val else 0.0


def average_balance(df=None):
    if df is not None:
        return round(float(df["balance"].mean()), 2) if not df.empty and "balance" in df else 0.0
    query = "SELECT AVG(balance) FROM customer_dashboard;"
    val = execute_scalar(query)
    return round(float(val), 2) if val else 0.0


def total_deposits(df=None):
    if df is not None:
        return float(df["deposits"].sum()) if not df.empty and "deposits" in df else 0.0
    query = "SELECT SUM(deposits) FROM customer_dashboard;"
    val = execute_scalar(query)
    return float(val) if val else 0.0


def risk_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "risk_tolerance" in active_df.columns:
        res = active_df.groupby("risk_tolerance").size().reset_index(name="customers")
        return res
    return pd.DataFrame(columns=["risk_tolerance", "customers"])


def occupation_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "occupation" in active_df.columns:
        res = active_df.groupby("occupation").size().reset_index(name="customers")
        return res
    return pd.DataFrame(columns=["occupation", "customers"])


def high_risk_customers(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "risk_tolerance" in active_df.columns:
        return active_df[active_df["risk_tolerance"].astype(str).str.lower() == "high"]
    return pd.DataFrame()


def approved_loans(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "loan_status" in active_df.columns:
        return active_df[active_df["loan_status"].astype(str).str.lower() == "approved"]
    return pd.DataFrame()


def customer_segments(df=None):
    active_df = _get_active_df(df)
    if active_df.empty:
        return pd.DataFrame(columns=["customer_id", "balance", "customer_segment"])
    
    def segment(b):
        if b >= 100000:
            return "Premium"
        elif b >= 50000:
            return "Gold"
        return "Regular"

    res = active_df[["customer_id", "balance"]].copy()
    res["customer_segment"] = res["balance"].apply(segment)
    return res


def total_accounts(df=None):
    if df is not None:
        return len(df)
    query = "SELECT COUNT(*) FROM account_dashboard;"
    return execute_scalar(query)


def total_loans(df=None):
    if df is not None:
        if "loan_amount" in df.columns:
            return len(df[df["loan_amount"].notna()])
        return len(df)
    query = "SELECT COUNT(*) FROM loan_dashboard;"
    return execute_scalar(query)


def total_transactions(df=None):
    if df is not None:
        return len(df)
    query = "SELECT COUNT(*) FROM transaction_dashboard;"
    return execute_scalar(query)


def average_monthly_income(df=None):
    if df is not None:
        if not df.empty and "income_level" in df.columns:
            vals = pd.to_numeric(df["income_level"], errors="coerce")
            return round(float(vals.mean()), 2)
        return 0.0
    query = "SELECT AVG(CAST(income_level AS REAL)) FROM customer_dashboard;"
    val = execute_scalar(query)
    return round(float(val), 2) if val else 0.0


def active_loans(df=None):
    if df is not None:
        if not df.empty and "loan_status" in df.columns:
            return len(df[df["loan_status"].astype(str).str.lower() == "approved"])
        return 0
    query = "SELECT COUNT(*) FROM loan_dashboard WHERE LOWER(loan_status)='approved';"
    return execute_scalar(query)


def average_loan_amount(df=None):
    if df is not None:
        if not df.empty and "loan_amount" in df.columns:
            vals = pd.to_numeric(df["loan_amount"], errors="coerce")
            return round(float(vals.mean()), 2)
        return 0.0
    query = "SELECT AVG(loan_amount) FROM loan_dashboard;"
    val = execute_scalar(query)
    return round(float(val), 2) if val else 0.0


def premium_customers(df=None):
    if df is not None:
        if not df.empty and "balance" in df.columns:
            return len(df[df["balance"] >= 100000])
        return 0
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE balance >= 100000;"
    return execute_scalar(query)


def high_balance_customers(df=None):
    if df is not None:
        if not df.empty and "balance" in df.columns:
            return len(df[df["balance"] >= 50000])
        return 0
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE balance >= 50000;"
    return execute_scalar(query)


def total_loan_portfolio(df=None):
    if df is not None:
        if not df.empty and "loan_amount" in df.columns and "loan_status" in df.columns:
            app = df[df["loan_status"].astype(str).str.lower() == "approved"]
            return float(app["loan_amount"].sum())
        return 0.0
    query = "SELECT SUM(loan_amount) FROM loan_dashboard WHERE LOWER(loan_status)='approved';"
    val = execute_scalar(query)
    return float(val) if val else 0.0


def account_type_counts(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "account_type" in active_df.columns:
        return active_df.groupby("account_type").size().reset_index(name="count")
    return pd.DataFrame(columns=["account_type", "count"])


def loan_status_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "loan_status" in active_df.columns:
        return active_df.groupby("loan_status").size().reset_index(name="count")
    return pd.DataFrame(columns=["loan_status", "count"])


def risk_tolerance_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "risk_tolerance" in active_df.columns:
        return active_df.groupby("risk_tolerance").size().reset_index(name="count")
    return pd.DataFrame(columns=["risk_tolerance", "count"])


def customers_per_region(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "region" in active_df.columns:
        return active_df.groupby("region").size().reset_index(name="count")
    return pd.DataFrame(columns=["region", "count"])


def top_occupations(df=None, limit=5):
    active_df = _get_active_df(df)
    if not active_df.empty and "occupation" in active_df.columns:
        res = (
            active_df.groupby("occupation")
            .size()
            .reset_index(name="count")
            .sort_values("count", ascending=False)
            .head(limit)
        )
        return res
    return pd.DataFrame(columns=["occupation", "count"])


def total_approved_loans(df=None):
    if df is not None:
        if not df.empty and "loan_status" in df.columns:
            return len(df[df["loan_status"].astype(str).str.lower() == "approved"])
        return 0
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE LOWER(loan_status)='approved';"
    return execute_scalar(query)


def total_high_risk_customers(df=None):
    if df is not None:
        if not df.empty and "risk_tolerance" in df.columns:
            return len(df[df["risk_tolerance"].astype(str).str.lower() == "high"])
        return 0
    query = "SELECT COUNT(*) FROM customer_dashboard WHERE LOWER(risk_tolerance)='high';"
    return execute_scalar(query)


def age_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "age" in active_df.columns:
        return active_df[["age"]].dropna()
    return pd.DataFrame(columns=["age"])


def region_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "region" in active_df.columns:
        return active_df.groupby("region").size().reset_index(name="customers")
    return pd.DataFrame(columns=["region", "customers"])


def balance_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "balance" in active_df.columns:
        return active_df[["balance"]].dropna()
    return pd.DataFrame(columns=["balance"])


def account_type_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "account_type" in active_df.columns:
        return active_df.groupby("account_type").size().reset_index(name="customers")
    return pd.DataFrame(columns=["account_type", "customers"])


def investment_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "investments" in active_df.columns:
        return active_df[["investments"]].dropna()
    return pd.DataFrame(columns=["investments"])


def deposits_vs_withdrawals(df=None):
    active_df = _get_active_df(df)
    dep = active_df["deposits"].sum() if "deposits" in active_df.columns else 0.0
    wth = active_df["withdrawals"].sum() if "withdrawals" in active_df.columns else 0.0
    return pd.DataFrame({
        "Metric": ["Deposits", "Withdrawals"],
        "Amount": [float(dep), float(wth)]
    })


def loan_purpose_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "loan_purpose" in active_df.columns:
        return active_df.groupby("loan_purpose").size().reset_index(name="count")
    return pd.DataFrame(columns=["loan_purpose", "count"])


def interest_rate_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "interest_rate" in active_df.columns:
        return active_df[["interest_rate"]].dropna()
    return pd.DataFrame(columns=["interest_rate"])


def loan_amount_distribution(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "loan_amount" in active_df.columns:
        return active_df[["loan_amount"]].dropna()
    return pd.DataFrame(columns=["loan_amount"])


def approval_by_risk(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "risk_tolerance" in active_df.columns and "loan_status" in active_df.columns:
        return (
            active_df.groupby(["risk_tolerance", "loan_status"])
            .size()
            .reset_index(name="customers")
        )
    return pd.DataFrame(columns=["risk_tolerance", "loan_status", "customers"])


def interest_vs_loan(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "loan_amount" in active_df.columns and "interest_rate" in active_df.columns:
        return active_df[["loan_amount", "interest_rate"]].dropna()
    return pd.DataFrame(columns=["loan_amount", "interest_rate"])


def _parse_time_series(df_source):
    records = []
    for idx, row in df_source.iterrows():
        c_id = str(row.get("customer_id", f"Customer_{idx}"))
        dates_raw = str(row.get("dates", ""))
        trans_raw = str(row.get("transactions", ""))
        rep_raw = str(row.get("repayments", ""))

        d_matches = DATE_PAT.findall(dates_raw)
        d_list = [f"{y}-{int(m):02d}-{int(d):02d}" for y, m, d in d_matches]
        
        t_list = [float(x) for x in NUM_PAT.findall(trans_raw)]
        r_list = [float(x) for x in NUM_PAT.findall(rep_raw)]

        n = min(len(d_list), len(t_list))
        for i in range(n):
            rep_val = r_list[i] if i < len(r_list) else 0.0
            records.append({
                "customer_id": c_id,
                "transaction_date": d_list[i],
                "transactions": t_list[i],
                "repayments": rep_val
            })
    if not records:
        return pd.DataFrame(columns=["customer_id", "transaction_date", "transactions", "repayments"])
    return pd.DataFrame(records)


def transaction_trend(df=None):
    active_df = _get_active_df(df)
    ts_df = _parse_time_series(active_df)
    if not ts_df.empty:
        trend = ts_df.groupby("transaction_date")["transactions"].sum().reset_index()
        trend.columns = ["transaction_date", "transactions"]
        return trend.sort_values("transaction_date")
    return pd.DataFrame(columns=["transaction_date", "transactions"])


def monthly_transactions(df=None):
    active_df = _get_active_df(df)
    ts_df = _parse_time_series(active_df)
    if not ts_df.empty:
        ts_df["month"] = pd.to_datetime(ts_df["transaction_date"], errors="coerce").dt.to_period("M").astype(str)
        monthly = ts_df.groupby("month")["transactions"].sum().reset_index()
        monthly.columns = ["month", "transactions"]
        return monthly.sort_values("month")
    return pd.DataFrame(columns=["month", "transactions"])


def transaction_type_distribution(df=None):
    active_df = _get_active_df(df)
    cols = ["deposits", "withdrawals", "transfers", "international_transfers", "investments"]
    labels = ["Deposits", "Withdrawals", "Transfers", "Intl Transfers", "Investments"]
    counts = []
    for col in cols:
        if col in active_df.columns:
            counts.append(int((active_df[col] > 0).sum()))
        else:
            counts.append(0)
    return pd.DataFrame({
        "transaction_type": labels,
        "count": counts
    })


def average_transaction_value(df=None):
    active_df = _get_active_df(df)
    cols = ["deposits", "withdrawals", "transfers", "international_transfers", "investments"]
    labels = ["Deposits", "Withdrawals", "Transfers", "Intl Transfers", "Investments"]
    avg_vals = []
    for col in cols:
        if col in active_df.columns:
            val = float(active_df[col].mean()) if not active_df.empty else 0.0
            avg_vals.append(round(val, 2))
        else:
            avg_vals.append(0.0)
    return pd.DataFrame({
        "transaction_type": labels,
        "average_value": avg_vals
    })


def repayment_trend(df=None):
    active_df = _get_active_df(df)
    ts_df = _parse_time_series(active_df)
    if not ts_df.empty:
        ts_df["month"] = pd.to_datetime(ts_df["transaction_date"], errors="coerce").dt.to_period("M").astype(str)
        rep = ts_df.groupby("month")["repayments"].sum().reset_index()
        rep.columns = ["month", "repayments"]
        return rep.sort_values("month")
    return pd.DataFrame(columns=["month", "repayments"])


def top_transaction_customers(df=None):
    active_df = _get_active_df(df)
    ts_df = _parse_time_series(active_df)
    if not ts_df.empty:
        top = ts_df.groupby("customer_id")["transactions"].count().reset_index(name="transactions")
        top["customer_name"] = top["customer_id"].apply(lambda x: f"Cust-{str(x)[:6]}")
        return top.sort_values("transactions", ascending=False).head(10)
    return pd.DataFrame(columns=["customer_id", "customer_name", "transactions"])


def income_vs_investment(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "income_level" in active_df.columns and "investments" in active_df.columns:
        return active_df[["income_level", "investments"]].dropna()
    return pd.DataFrame(columns=["income_level", "investments"])


def customer_segmentation(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "income_level" in active_df.columns and "balance" in active_df.columns and "risk_tolerance" in active_df.columns:
        return active_df[["income_level", "balance", "risk_tolerance"]].dropna()
    return pd.DataFrame(columns=["income_level", "balance", "risk_tolerance"])


def occupation_balance(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "occupation" in active_df.columns and "balance" in active_df.columns:
        return active_df.groupby("occupation")["balance"].mean().reset_index(name="average_balance")
    return pd.DataFrame(columns=["occupation", "average_balance"])


def risk_vs_investment(df=None):
    active_df = _get_active_df(df)
    if not active_df.empty and "risk_tolerance" in active_df.columns and "investments" in active_df.columns:
        return active_df[["risk_tolerance", "investments"]].dropna()
    return pd.DataFrame(columns=["risk_tolerance", "investments"])
