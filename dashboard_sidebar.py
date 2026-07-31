import streamlit as st
import pandas as pd


# ============================================================
# Helper Function
# ============================================================

def create_multiselect_filter(
    filtered_df: pd.DataFrame,
    original_df: pd.DataFrame,
    column: str,
    label: str,
) -> pd.DataFrame:
    """
    Creates a reusable multiselect filter.

    Parameters
    ----------
    filtered_df : DataFrame
        Current filtered dataframe.

    original_df : DataFrame
        Original dataframe (used for all available options).

    column : str
        Column name.

    label : str
        Sidebar label.

    Returns
    -------
    DataFrame
        Updated filtered dataframe.
    """

    # Skip if column doesn't exist
    if column not in original_df.columns:
        return filtered_df

    options = (
        original_df[column]
        .dropna()
        .astype(str)
        .sort_values()
        .unique()
        .tolist()
    )

    selected = st.sidebar.multiselect(
        label=label,
        options=options,
        default=[]
    )

    if selected:
        filtered_df = filtered_df[
            filtered_df[column].astype(str).isin(selected)
        ]

    return filtered_df


# ============================================================
# Main Sidebar
# ============================================================

def sidebar_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates the dashboard sidebar.

    Parameters
    ----------
    df : DataFrame

    Returns
    -------
    DataFrame
        Filtered dataframe.
    """

    # -------------------------
    # Validation
    # -------------------------

    if df is None:
        st.error("No dataframe received.")
        return pd.DataFrame()

    if df.empty:
        st.warning("Dataset is empty.")
        return df

    # -------------------------
    # Sidebar Header
    # -------------------------

    st.sidebar.title("🏦 FinTech Dashboard")

    st.sidebar.markdown("---")

    st.sidebar.subheader("Filters")

    filtered_df = df.copy()

    # =========================================================
    # Customer Filters
    # =========================================================

    filtered_df = create_multiselect_filter(
        filtered_df,
        df,
        "region",
        "🌍 Region"
    )

    filtered_df = create_multiselect_filter(
        filtered_df,
        df,
        "occupation",
        "💼 Occupation"
    )

    filtered_df = create_multiselect_filter(
        filtered_df,
        df,
        "risk_tolerance",
        "⚠️ Risk Category"
    )

    # =========================================================
    # Loan Filters
    # =========================================================

    filtered_df = create_multiselect_filter(
        filtered_df,
        df,
        "loan_status",
        "🏦 Loan Status"
    )

    # =========================================================
    # Account Filters
    # =========================================================

    filtered_df = create_multiselect_filter(
        filtered_df,
        df,
        "account_type",
        "💳 Account Type"
    )

    st.sidebar.markdown("---")

    # =========================================================
    # Dataset Summary
    # =========================================================

    st.sidebar.subheader("Dataset Summary")

    st.sidebar.metric(
        label="Visible Records",
        value=f"{len(filtered_df):,}"
    )

    st.sidebar.metric(
        label="Filtered Out",
        value=f"{len(df)-len(filtered_df):,}"
    )

    # =========================================================
    # Reset Button
    # =========================================================

    if st.sidebar.button(
        "Reset Filters",
        use_container_width=True
    ):
        st.rerun()

    return filtered_df