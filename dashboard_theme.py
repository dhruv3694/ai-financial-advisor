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

        section[data-testid="stSidebar"]{
            background-color:white;
            border-right:1px solid #e5e7eb;
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