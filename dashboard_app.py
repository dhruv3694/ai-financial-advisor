import streamlit as st

from dashboard_theme import apply_theme
from dashboard_sidebar import sidebar_filters
from dashboard_pages import render_dashboard


# Configure Streamlit

st.set_page_config(
    page_title="FinTech Analytics Dashboard",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Apply Theme

apply_theme()


