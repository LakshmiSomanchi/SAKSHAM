import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px

# --- Configuration ---
PAGE_TITLE = "SAKSHAM Baseline Survey Dashboard"
PAGE_ICON = "🌍"
LAYOUT = "wide"
INITIAL_SIDEBAR_STATE = "expanded"

# --- Datawrapper Embed Definitions ---
# Centralize all Datawrapper embed codes and their properties
# We'll extract the min-height from the embed code and add a buffer for uniformity and full display.
DATAWRAPPER_EMBEDS = {
    # Geographic Data Maps
    "geo_map_1_overview_distribution": {
        "code": """<div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 598 # Extracted from the div's style
    },
    "geo_map_2_additional_regional_view": {
        "code": """<div style="min-height:384px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 384
    },
    "geo_map_3_further_geographic_insight": {
        "code": """<div style="min-height:677px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 677
    },
    "geo_map_4_quick_geographic_detail": {
        "code": """<div style="min-height:114px" id="datawrapper-vis-fNesy"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/fNesy/embed.js" charset="utf-8" data-target="#datawrapper-vis-fNesy"></script><noscript><img src="https://datawrapper.dwcdn.net/fNesy/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 114
    },
    "geo_map_5_detailed_view": {
        "code": """<div style="min-height:558px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 558
    },
    # Demographic Data Charts
    "demographic_household_composition": {
        "code": """<div style="min-height:451px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 451
    },
    # Environmental Data Charts
    "env_source_of_irrigation": {
        "code": """<div style="min-height:258px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 258
    },
    "env_avg_organic_cotton_production": {
        "code": """<div style="min-height:468px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 468
    },
}

# --- Page Setup ---
def setup_page():
    """Sets up the basic Streamlit page configuration and title."""
    st.set_page_config(
        page_title=PAGE_TITLE,
        page_icon=PAGE_ICON,
        layout=LAYOUT,
        initial_sidebar_state=INITIAL_SIDEBAR_STATE
    )
    st.title(f"📊 {PAGE_TITLE}")
    st.write("This dashboard provides an overview of SAKSHAM's baseline survey parameters.")

# --- Helper Function for Displaying Datawrapper Embeds ---
def display_datawrapper_embed(key, buffer=30):
    """
    Displays a Datawrapper embed based on its key from the DATAWRAPPER_EMBEDS dictionary.
    Calculates height based on min_height_from_embed plus a buffer.
    """
    if key in DATAWRAPPER_EMBEDS:
        embed_info = DATAWRAPPER_EMBEDS[key]
        # Calculate the display height: min_height from embed + buffer
        display_height = embed_info["min_height_from_embed"] + buffer
        components.html(embed_info["code"], height=display_height, scrolling=False)
    else:
        st.error(f"Error: Datawrapper embed with key '{key}' not found in configuration.")

# --- Tab Content Functions ---

def render_geographic_data_tab():
    """Renders the content for the Geographic Data tab."""
    st.header("Geographic Overview")
    st.write("Select a map below to view its details.")

    geo_map_options_display = {
        "Map 1: Overview Distribution": "geo_map_1_overview_distribution",
        "Map 2: Additional Regional View": "geo_map_2_additional_regional_view",
        "Map 3: Further Geographic Insight": "geo_map_3_further_geographic_insight",
        "Map 4: Quick Geographic Detail": "geo_map_4_quick_geographic_detail",
        "Map 5: Detailed Geographic View": "geo_map_5_detailed_view",
    }

    selected_geo_map_name = st.radio(
        "Choose a geographic map to display:",
        list(geo_map_options_display.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_geo_map_name:
        selected_key = geo_map_options_display[selected_geo_map_name]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Please select a geographic map from the options above.")

def render_demographic_data_tab():
    """Renders the content for the Demographic Data tab."""
    st.header("Demographic Data")
    st.write("Explore insights into household composition and other demographic trends.")

    demographic_chart_options_display = {
        "Household Composition": "demographic_household_composition",
        # Add other demographic charts here if needed, mapping display name to DATAWRAPPER_EMBEDS key
    }

    selected_demographic_chart = st.radio(
        "Choose a demographic chart to display:",
        list(demographic_chart_options_display.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_demographic_chart:
        selected_key = demographic_chart_options_display[selected_demographic_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Please select a demographic chart from the options above.")

def render_economic_data_tab():
    """Renders the content for the Economic Data tab."""
    st.header("Economic Data")
    st.write("View economic indicators such as organic cotton certification status.")

    economic_chart_options_display = {
        # This section is currently empty as per your previous request
        # Example if you add one: "Certification Status": "economic_certification_status",
    }

    if economic_chart_options_display: # Only show radio if there are options
        selected_economic_chart = st.radio(
            "Choose an economic chart to display:",
            list(economic_chart_options_display.keys()),
            horizontal=True
        )
        st.markdown("---")
        selected_key = economic_chart_options_display[selected_economic_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Content for this section will be added soon. (Economic charts are currently empty)")

def render_social_data_tab():
    """Renders the content for the Social Data tab."""
    st.header("Social Data")
    st.write("This section will cover parameters like labour register maintenance and participation in government schemes.")
    st.info("Content for this section will be added soon.")

def render_environmental_data_tab():
    """Renders the content for the Environmental Data tab."""
    st.header("Environmental Data")
    st.write("This section presents data on crop residue management, irrigation sources, and organic cotton production.")

    environmental_chart_options_display = {
        "Source of Irrigation": "env_source_of_irrigation",
        "Avg. production of organic cotton/acre (Kg)": "env_avg_organic_cotton_production",
    }

    selected_environmental_chart = st.radio(
        "Choose an environmental chart to display:",
        list(environmental_chart_options_display.keys()),
        horizontal=True
    )

    st.markdown("---")

    if selected_environmental_chart:
        selected_key = environmental_chart_options_display[selected_environmental_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Please select an environmental chart from the options above.")

# --- Main Application Logic ---
def main():
    """Main function to run the Streamlit dashboard."""
    setup_page()

    tab_geographic, tab_demographic, tab_economic, tab_social, tab_environmental = st.tabs([
        "🌍 Geographic Data",
        "🧑‍🤝‍👩 Demographic Data",
        "💰 Economic Data",
        "🤝 Social Data",
        "🌱 Environmental Data"
    ])

    with tab_geographic:
        render_geographic_data_tab()

    with tab_demographic:
        render_demographic_data_tab()

    with tab_economic:
        render_economic_data_tab()

    with tab_social:
        render_social_data_tab()

    with tab_environmental:
        render_environmental_data_tab()

if __name__ == "__main__":
    main()
