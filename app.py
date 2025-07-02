import streamlit as st
import streamlit.components.v1 as components
import pandas as pd # Re-import pandas for dummy data if you add native charts later
import numpy as np # Re-import numpy for dummy data if you add native charts later
import plotly.express as px # Re-import plotly for dummy data if you add native charts later

# --- Page Configuration (MUST be the first Streamlit command) ---
st.set_page_config(
    page_title="SAKSHAM Baseline Survey Dashboard",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Dashboard Title ---
st.title("📊 SAKSHAM Baseline Survey Dashboard")
st.write("This dashboard provides an overview of SAKSHAM's baseline survey parameters.")

# --- Dashboard Sections using Tabs ---
tab_geographic, tab_demographic, tab_economic, tab_social, tab_environmental = st.tabs([
    "🌍 Geographic Data",
    "🧑‍🤝‍👩 Demographic Data",
    "💰 Economic Data",
    "🤝 Social Data",
    "🌱 Environmental Data"
])

# --- Content for 'Geographic Data' Tab ---
with tab_geographic:
    st.header("Geographic Overview")
    st.write("Select a map below to view its details.")

    # Define the options for the radio buttons in Geographic Data
    geo_map_options = {
        "Map 1: Overview Distribution (Oq2xV)": {
            "code": """
            <div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
            """,
            "height": 620 # Increased from 650 to ensure full visibility if title/legend slightly expand
        },
        "Map 2: Additional Regional View (dNfZU)": {
            "code": """
            <div style="min-height:384px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>
            """,
            "height": 410 # Increased from 450
        },
        "Map 3: Further Geographic Insight (7IEJR - Original Geo Map)": { # Renamed for clarity
            "code": """
            <div style="min-height:677px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>
            """,
            "height": 700 # Increased from 730
        },
        "Map 4: Quick Geographic Detail (fNesy)": {
            "code": """
            <div style="min-height:114px" id="datawrapper-vis-fNesy"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/fNesy/embed.js" charset="utf-8" data-target="#datawrapper-vis-fNesy"></script><noscript><img src="https://datawrapper.dwcdn.net/fNesy/full.png" alt="" /></noscript></div>
            """,
            "height": 140 # Increased from 180
        },
        "Map 5: Detailed Geographic View (3Fewz - Original Geo Map)": { # Renamed for clarity
            "code": """
            <div style="min-height:558px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>
            """,
            "height": 580 # Increased from 620
        },
    }

    selected_geo_map_name = st.radio(
        "Choose a geographic map to display:",
        list(geo_map_options.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_geo_map_name:
        map_info = geo_map_options[selected_geo_map_name]
        components.html(map_info["code"], height=map_info["height"], scrolling=False)
    else:
        st.info("Please select a geographic map from the options above.")


# --- Content for 'Demographic Data' Tab ---
with tab_demographic:
    st.header("Demographic Data")
    st.write("Explore insights into household composition and other demographic trends.")

    # Define options for demographic charts
    demographic_chart_options = {
        "Household Composition": { # This is the new chart
            "code": """
            <div style="min-height:565px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>
            """,
            "height": 590 # Adjusted height, ensuring it's slightly more than min-height
        },
        # You can add more demographic charts here later
        # "Gender Distribution (Dummy)": {
        #     "type": "plotly",
        #     "data_func": lambda: pd.DataFrame({'Category': ['Male', 'Female'], 'Count': [np.random.randint(50, 150), np.random.randint(50, 150)]}),
        #     "chart_func": lambda df: px.pie(df, values='Count', names='Category', title='Gender Distribution')
        # },
    }

    selected_demographic_chart = st.radio(
        "Choose a demographic chart to display:",
        list(demographic_chart_options.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_demographic_chart:
        chart_info = demographic_chart_options[selected_demographic_chart]
        components.html(chart_info["code"], height=chart_info["height"], scrolling=False)
    else:
        st.info("Please select a demographic chart from the options above.")


# --- Content for 'Economic Data' Tab ---
with tab_economic:
    st.header("Economic Data")
    st.write("View economic indicators such as organic cotton production and certification status.")

    # Define options for economic charts
    economic_chart_options = {
        "Avg. Production of Organic Cotton/Acre (Kg)": { # This is the new chart
            "code": """
            <div style="min-height:558px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>
            """,
            "height": 580 # Adjusted height, ensuring it's slightly more than min-height
        },
        # You can add more economic charts here later
        # "Certification Status (Dummy)": {
        #     "type": "plotly",
        #     "data_func": lambda: pd.DataFrame({'Status': ['Certified', 'Not Certified'], 'Count': [np.random.randint(30, 80), np.random.randint(80, 150)]}),
        #     "chart_func": lambda df: px.pie(df, values='Count', names='Status', title='Certification Status')
        # },
    }

    selected_economic_chart = st.radio(
        "Choose an economic chart to display:",
        list(economic_chart_options.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_economic_chart:
        chart_info = economic_chart_options[selected_economic_chart]
        components.html(chart_info["code"], height=chart_info["height"], scrolling=False)
    else:
        st.info("Please select an economic chart from the options above.")


# --- Content for 'Social Data' Tab ---
with tab_social:
    st.header("Social Data")
    st.write("This section will cover parameters like labour register maintenance and participation in government schemes.")
    st.info("Content for this section will be added soon.")

# --- Content for 'Environmental Data' Tab ---
with tab_environmental:
    st.header("Environmental Data")
    st.write("This section will present data on crop residue management, irrigation sources, and number of irrigations.")
    st.info("Content for this section will be added soon.")
    
