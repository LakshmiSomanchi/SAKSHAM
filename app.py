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
        # Use a key to ensure Streamlit re-renders if content changes (good practice for dynamic HTML)
        components.html(html_content, height=default_height, scrolling=True, key=file_name)
    except FileNotFoundError:
        st.error(f"Error: `{file_name}` not found. Please ensure it's in the same directory as app.py.")
        st.info("The content for this section could not be loaded.")
        st.warning("If deploying to Streamlit Cloud, verify all HTML files are pushed to GitHub.")


# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide", # Use a wide layout to maximize space for the dashboard
    initial_sidebar_state="expanded", # Expanded sidebar for tab navigation if needed
    menu_items={
        'Get Help': 'https://www.google.com/search?q=saksham+project+support',
        'Report a bug': "https://github.com/LakshmiSomanchi/SAKSHAM/issues", # REMINDER: Update this to your actual repo's issues page
        'About': "# SAKSHAM Project Dashboard\nThis dashboard provides an comprehensive overview of key metrics for the SAKSHAM Cotton Project. Visualizations are sourced directly from Datawrapper embeds within the core HTML structure."
    }
)

# --- Main Dashboard Header ---
st.title(" SAKSHAM Project: Comprehensive Dashboard")
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
    " Overview & KPIs",
    " Demographic Data",
    " Economic Insights",
    " Social Indicators",
    " Environmental Data"
])

# Content for each tab, loading the specific HTML files
with tab_overview:
    st.header("Overview & Key Performance Indicators")
    st.markdown("This section provides a quick snapshot of the project's reach and key metrics.")
    # Assuming SAKSHAM.html contains your overview and KPIs
    load_html_component("SAKSHAM.html", default_height=250)

with tab_demographic:
    st.header("Demographic Data")
    st.markdown("Explore the geographical distribution and population composition of the project areas.")
    # This height is adjusted for the original SAKSHAM map, household, gender, and the new Maharashtra map.
    # Estimated sum of min-heights + padding/titles: 598 + 451 + 114 + 603 + ~200 = ~1966. Set to 2000.
    load_html_component("page2.html", default_height=2000)

with tab_economic:
    st.header("Economic Insights")
    st.markdown("Understand the economic aspects, including yield and farmer certification.")
    # This height is adjusted for Avg Production (468px) + Yield (466px) + 1 placeholder + padding/titles
    # 468 + 466 + ~100 = ~1034. Set to 1100.
    load_html_component("page3.html", default_height=1100)

with tab_social:
    st.header("Social Indicators")
    st.markdown("View data related to social welfare, labor, and government scheme adoption.")
    # This height is adjusted for Labour Registry (368px) + Govt Schemes (132px) + padding/titles
    # 368 + 132 + ~100 = ~600. Set to 700.
    load_html_component("page4.html", default_height=700)

with tab_environmental:
    st.header("Environmental Data")
    st.markdown("Discover insights into environmental practices and resource management.")
    # This height is adjusted for Irrigation (258px) + Crop Residue (558px) + 1 placeholder + padding/titles
    # 258 + 558 + ~100 = ~916. Set to 1000.
    load_html_component("page5.html", default_height=1000)


# --- Streamlit Footer ---
st.markdown("---")
st.markdown("© 2025 SAKSHAM Project. All rights reserved.")
st.markdown("Dashboard developed using Streamlit and Datawrapper embeds.")
st.markdown(f"**Data displayed is current as of:** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
