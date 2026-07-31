import streamlit as st


# ===========================================
# KPI Card
# ===========================================

def create_metric_card(
    title,
    value,
    delta=None,
    help_text=None
):

    st.metric(
        label=title,
        value=value,
        delta=delta,
        help=help_text
    )


# ===========================================
# Section Header
# ===========================================

def create_section_header(title):

    st.markdown(f"## {title}")


# ===========================================
# Chart Container
# ===========================================

def create_chart_container(fig):

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ===========================================
# Information Box
# ===========================================

def create_info_box(message):

    st.info(message)


# ===========================================
# Divider
# ===========================================

def create_divider():

    st.divider()