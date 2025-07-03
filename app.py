import streamlit as st
import streamlit.components.v1 as components
import os
import datetime

# --- Helper function to load HTML content ---
def load_html_component(file_name, default_height=700):
    """Loads an HTML file and embeds it using Streamlit components.html."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=default_height, scrolling=True)
    except FileNotFoundError:
        st.error(f"Error: `{file_name}` not found. Please ensure it's in the same directory.")
        st.info("The content for this section could not be loaded.")

# --- Streamlit Page Configuration (rest of your config...) ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/search?q=saksham+project+support',
        'Report a bug': "https://github.com/your-username/your-repo-name/issues",
        'About': "# SAKSHAM Project Dashboard\nThis dashboard provides an comprehensive overview of key metrics for the SAKSHAM Cotton Project. Visualizations are sourced directly from Datawrapper embeds within the core HTML structure."
    }
)

# --- Main Dashboard Header (rest of your header...) ---
st.title("SAKSHAM Project: Comprehensive Dashboard")
st.markdown("""
Welcome to the interactive dashboard for the SAKSHAM Cotton Project.
Navigate through the tabs below to explore different aspects of the project, including demographic data, economic insights, social indicators, and environmental practices.
""")
st.markdown("---")


# --- Streamlit Tabs for Navigation ---
tab_overview, tab_demographic, tab_economic, tab_social, tab_environmental = st.tabs([
    "Overview & KPIs",
    "Demographic Data",
    "Economic Insights",
    "Social Indicators",
    "Environmental Data"
])

# Content for each tab - MODIFIED FILE NAMES HERE
with tab_overview:
    st.header("Overview & Key Performance Indicators")
    st.markdown("This section provides a quick snapshot of the project's reach and key metrics.")
    load_html_component("SAKSHAM.html", default_height=250) # Use your SAKSHAM.html for overview

with tab_demographic:
    st.header("Demographic Data")
    st.markdown("Explore the geographical distribution and population composition of the project areas.")
    load_html_component("page2.html", default_height=1400) # Assuming page2.html is demographic

with tab_economic:
    st.header("Economic Insights")
    st.markdown("Understand the economic aspects, including yield and farmer certification.")
    load_html_component("page3.html", default_height=1000) # Assuming page3.html is economic

with tab_social:
    st.header("Social Indicators")
    st.markdown("View data related to social welfare, labor, and government scheme adoption.")
    load_html_component("page4.html", default_height=700) # Assuming page4.html is social

with tab_environmental:
    st.header("Environmental Data")
    st.markdown("Discover insights into environmental practices and resource management.")
    load_html_component("page5.html", default_height=1000) # Assuming page5.html is environmental

# --- Streamlit Sidebar (rest of your sidebar...) ---
with st.sidebar:
    st.header("About SAKSHAM Dashboard")
    st.markdown("""
    This dashboard serves as a central hub for visualizing critical data from the SAKSHAM Cotton Project.
    All charts and data visualizations are powered by interactive Datawrapper embeds, ensuring a rich and dynamic user experience.
    """)
    st.markdown("---")
    st.subheader("Project Links")
    st.write("[Learn more about SAKSHAM Project](https://example.com/saksham-project)")
    st.write("[Project Documentation](https://example.com/docs)")
    st.markdown("---")
    st.subheader("Contact & Support")
    st.write("For support, please email: `bkharoo@tns.org`, 'ksuneha@tns.org'")
    st.markdown("---")
    st.caption(f"Dashboard App Version 1.0")
    st.caption(f"Last App Deployment/Refresh: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")


# --- Streamlit Footer (rest of your footer...) ---
st.markdown("---")
st.markdown("© 2025 SAKSHAM Project. All rights reserved.")
st.markdown("Dashboard developed using Streamlit and Datawrapper embeds.")
