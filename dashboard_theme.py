# like CSS-styling and design for our dashboard
import streamlit as st


def apply_theme():

    st.markdown(
        """
        <style>

        /* -----------------------------
           Main Page
        ------------------------------*/

        .main{
            background-color:#f8fafc;
        }

        .block-container{
            padding-top:1.5rem;
            padding-bottom:2rem;
            padding-left:2rem;
            padding-right:2rem;
        }

        /* -----------------------------
           Sidebar
        ------------------------------*/

        section[data-testid="stSidebar"] {
            background-color: #0f172a !important;
            border-right: 1px solid #1e293b;
        }

        /* Sidebar Title and Subheaders */
        section[data-testid="stSidebar"] h1, 
        section[data-testid="stSidebar"] h2, 
        section[data-testid="stSidebar"] h3, 
        section[data-testid="stSidebar"] h4,
        section[data-testid="stSidebar"] .st-emotion-cache-10trblm {
            color: #f8fafc !important;
        }

        /* Sidebar labels and general text */
        section[data-testid="stSidebar"] label,
        section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p,
        section[data-testid="stSidebar"] p {
            color: #cbd5e1 !important;
            font-weight: 500;
        }

        /* Sidebar Horizontal Rules */
        section[data-testid="stSidebar"] hr {
            border-color: #1e293b !important;
        }

        /* Sidebar Metrics */
        section[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
            color: #94a3b8 !important;
        }
        section[data-testid="stSidebar"] [data-testid="stMetricValue"] {
            color: #f8fafc !important;
            font-weight: 700;
        }

        /* Multiselect Styling inside Sidebar */
        section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
            background-color: #1e293b !important;
            border-color: #334155 !important;
        }

        /* Style all elements and text/placeholder inside multiselect to be readable */
        section[data-testid="stSidebar"] div[data-baseweb="select"] * {
            color: #cbd5e1 !important;
        }

        /* Multiselect selected items (chips/tags) and their labels */
        section[data-testid="stSidebar"] div[role="button"] {
            background-color: #334155 !important;
        }

        section[data-testid="stSidebar"] div[role="button"] * {
            color: #f8fafc !important;
        }

        section[data-testid="stSidebar"] div[data-baseweb="select"] svg {
            fill: #cbd5e1 !important;
        }

        /* Sidebar Buttons */
        section[data-testid="stSidebar"] button[kind="secondary"] {
            background-color: #2563eb !important;
            color: white !important;
            border: 1px solid #3b82f6 !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }

        section[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background-color: #1d4ed8 !important;
            border-color: #2563eb !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06) !important;
        }

        /* -----------------------------
           Headers
        ------------------------------*/

        h1{
            color:#1e293b;
            font-weight:700;
        }

        h2{
            color:#334155;
        }

        h3{
            color:#475569;
        }

        /* -----------------------------
           Plotly Charts
        ------------------------------*/

        .stPlotlyChart{
            padding-top:10px;
            padding-bottom:10px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )