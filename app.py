import streamlit as st
import streamlit.components.v1 as components
import os
import datetime

# --- Helper function to load HTML content ---
def load_html_component(file_name, default_height=700):
    """Loads an HTML file and embeds it using Streamlit components.html."""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)

    st.write(f"DEBUG: Attempting to load: {file_path}") # Debug print
    html_content = "" # Initialize html_content to an empty string

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File does not exist: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        if not html_content.strip(): # Check if content is empty or just whitespace
            st.warning(f"DEBUG: HTML file `{file_name}` was found but appears to be empty or only contains whitespace.")
            # Provide a fallback message in the UI if content is empty
            components.html("<div><p>No content to display for this section.</p></div>", height=50, scrolling=False)
            return # Exit the function

        st.write(f"DEBUG: Successfully read `{file_name}`. Content length: {len(html_content)} characters.") # Debug print
        components.html(html_content, height=default_height, scrolling=True, key=file_name)

    except FileNotFoundError as e:
        st.error(f"""
            **Dashboard HTML file not found!**
            **Error:** `{e}`
            Please ensure that `{file_name}` is located in the same directory as `app.py`.
            Current expected path: `{file_path}`
            If you are running this locally, verify the file path.
            If deploying to Streamlit Cloud, ensure both files are pushed to your GitHub repository.
        """)
        # Provide a visual fallback for missing content
        st.image("https://via.placeholder.com/800x400.png?text=Content+Missing", use_column_width=True)
        st.warning(f"The content for section `{file_name}` cannot be displayed.")
    except Exception as e: # Catch any other unexpected errors during file processing
        st.error(f"An unexpected error occurred while loading `{file_name}`: {e}")
        st.info("Please check the file content for formatting issues.")


# --- Streamlit Page Configuration (rest of your config...) ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com/search?q=saksham+project+support',
        'Report a bug': "https://github.com/LakshmiSomanchi/SAKSHAM/issues", # REMINDER: Update this to your actual repo's issues page
        'About': "# SAKSHAM Project Dashboard\nThis dashboard provides an comprehensive overview of key metrics for the SAKSHAM Cotton Project. Visualizations are sourced directly from Datawrapper embeds within the core HTML structure."
    }
)

# --- Main Dashboard Header (rest of your header...) ---
st.title("🌱 SAKSHAM Project: Comprehensive Dashboard")
st.markdown("""
Welcome to the interactive dashboard for the SAKSHAM Cotton Project.
Navigate through the tabs below to explore different aspects of the project, including demographic data, economic insights, social indicators, and environmental practices.
""")
st.markdown("---")


# --- Streamlit Sidebar (rest of your sidebar...) ---
with st.sidebar:
    st.header("Dashboard Controls")
    st.info("This sidebar can be used for filters, navigation, or additional information.")
    st.markdown("---")
    st.markdown("Developed by the SAKSHAM Project Team.")
    st.caption(f"App deployed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")


# --- Streamlit Tabs for Navigation ---
tab_overview, tab_demographic, tab_economic, tab_social, tab_environmental = st.tabs([
    "🚀 Overview & KPIs",
    "🧑‍🤝‍👩 Demographic Data",
    "💰 Economic Insights",
    "🤝 Social Indicators",
    "🌳 Environmental Data"
])

# Content for each tab, loading the specific HTML files
with tab_overview:
    st.header("Overview & Key Performance Indicators")
    st.markdown("This section provides a quick snapshot of the project's reach and key metrics.")
    load_html_component("SAKSHAM.html", default_height=250)

with tab_demographic:
    st.header("Demographic Data")
    st.markdown("Explore the geographical distribution and population composition of the project areas.")
    load_html_component("page2.html", default_height=2000)

with tab_economic:
    st.header("Economic Insights")
    st.markdown("Understand the economic aspects, including yield and farmer certification.")
    load_html_component("page3.html", default_height=1100)

with tab_social:
    st.header("Social Indicators")
    st.markdown("View data related to social welfare, labor, and government scheme adoption.")
    load_html_component("page4.html", default_height=700)

with tab_environmental:
    st.header("Environmental Data")
    st.markdown("Discover insights into environmental practices and resource management.")
    load_html_component("page5.html", default_height=1000)


# --- Streamlit Footer (rest of your footer...) ---
st.markdown("---")
st.markdown("© 2025 SAKSHAM Project. All rights reserved.")
st.markdown("Dashboard developed using Streamlit and Datawrapper embeds.")
st.markdown(f"**Data displayed is current as of:** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
