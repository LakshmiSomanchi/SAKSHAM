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
        components.html(html_content, height=default_height, scrolling=True, key=file_name)
    except FileNotFoundError:
        st.error(f"Error: `{file_name}` not found. Please ensure it's in the same directory.")
        st.info("The content for this section could not be loaded.")

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/search?q=saksham+project+support',
        'Report a bug': "https://github.com/your-username/your-repo-name/issues", # REMINDER: Update this to your repo
        'About': "# SAKSHAM Project Dashboard\nThis dashboard provides an comprehensive overview of key metrics for the SAKSHAM Cotton Project. Visualizations are sourced directly from Datawrapper embeds within the core HTML structure."
    }
)

# --- Main Dashboard Header ---
st.title("SAKSHAM Project: Comprehensive Dashboard")
st.markdown("""
Welcome to the interactive dashboard for the SAKSHAM Cotton Project.
Navigate through the tabs below to explore different aspects of the project, including demographic data, economic insights, social indicators, and environmental practices.
""")
st.markdown("---")


# --- Streamlit Sidebar (Optional) ---
with st.sidebar:
    st.header("Dashboard Controls")
    st.info("This sidebar can be used for filters, navigation, or additional information.")
    st.markdown("---")
    st.markdown("Developed by the SAKSHAM Project Team.")
    st.caption(f"App deployed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")


# --- Streamlit Tabs for Navigation ---
tab_overview, tab_demographic, tab_economic, tab_social, tab_environmental = st.tabs([
    "Overview & KPIs",
    "Demographic Data",
    "Economic Insights",
    "Social Indicators",
    "Environmental Data"
])

# Content for each tab
with tab_overview:
    st.header("Overview & Key Performance Indicators")
    st.markdown("This section provides a quick snapshot of the project's reach and key metrics.")
    load_html_component("index_overview.html", default_height=250) # Height for KPI section

with tab_demographic:
    st.header("Demographic Data")
    st.markdown("Explore the geographical distribution and population composition of the project areas.")
    # Height adjusted for:
    # SAKSHAM Locations (598px)
    # Household Composition (451px)
    # Gender Ratio (114px)
    # Maharashtra Map (603px)
    # Plus titles, gaps, and padding (~150-200px)
    # 598 + 451 + 114 + 603 + 200 = ~1966. Setting to 2000 for safety.
    load_html_component("section_demographic.html", default_height=2000) # Adjusted height significantly

with tab_economic:
    st.header("Economic Insights")
    st.markdown("Understand the economic aspects, including yield and farmer certification.")
    load_html_component("section_economic.html", default_height=1100) # Keep this height if it was working well

with tab_social:
    st.header("Social Indicators")
    st.markdown("View data related to social welfare, labor, and government scheme adoption.")
    load_html_component("section_social.html", default_height=700) # Keep this height if it was working well

with tab_environmental:
    st.header("Environmental Data")
    st.markdown("Discover insights into environmental practices and resource management.")
    load_html_component("section_environmental.html", default_height=1000) # Keep this height if it was working well

# --- Streamlit Sidebar (Optional, continued from above for clarity) ---
# ... (rest of your sidebar content)


# --- Streamlit Footer ---
st.markdown("---")
st.markdown("© 2025 SAKSHAM Project. All rights reserved.")
st.markdown("Dashboard developed using Streamlit and Datawrapper embeds.")
st.markdown(f"**Data displayed is current as of:** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
