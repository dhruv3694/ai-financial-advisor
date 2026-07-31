import streamlit as st
import pandas as pd

# ===========================================
# Dashboard
# ===========================================

from dashboard_theme import apply_theme
from dashboard_sidebar import sidebar_filters
from dashboard_pages import render_dashboard

# ===========================================
# Analytics
# ===========================================

from data_analytics import customer_dashboard


# ===========================================
# Streamlit Configuration
# ===========================================

st.set_page_config(
    page_title="FinTech Analytics Dashboard",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ===========================================
# Theme
# ===========================================

apply_theme()


# ===========================================
# Load Data
# ===========================================

@st.cache_data
def load_dashboard():

    return customer_dashboard()


df = load_dashboard()


# ===========================================
# Sidebar
# ===========================================

filtered_df = sidebar_filters(df)


# ===========================================
# Dashboard
# ===========================================

render_dashboard(filtered_df)


# ===========================================
# Footer
# ===========================================

st.markdown("---")

st.caption(
    "FinTech Analytics Dashboard • Built with Python, SQLite, Pandas, Plotly and Streamlit"
)