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
# ONLY GEOGRAPHIC MAPS ARE KEPT HERE.
# You will add new embed codes for other sections when ready.
DATAWRAPPER_EMBEDS = {
    # Geographic Data Maps (Retained)
    "geo_map_1_overview_distribution": {
        "code": """<div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>""",
        "min_height_from_embed": 598
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
    # Other charts will be added here once you provide new embed codes.
    # Example for when you add a new chart:
    # "new_demographic_chart": {
    #     "code": """<div style="min-height:XYZpx" id="datawrapper-vis-ABCDE"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/ABCDE/embed.js" charset="utf-8" data-target="#datawrapper-vis-ABCDE"></script><noscript><img src="https://datawrapper.dwcdn.net/ABCDE/full.png" alt="" /></noscript></div>""",
    #     "min_height_from_embed": XYZ
    # },
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

    # This dictionary will be populated with new charts when you provide them.
    demographic_chart_options_display = {
        # Example when you add a new demographic chart:
        # "New Demographic Chart Title": "new_demographic_chart_key_from_DATAWRAPPER_EMBEDS",
    }

    if demographic_chart_options_display:
        selected_demographic_chart = st.radio(
            "Choose a demographic chart to display:",
            list(demographic_chart_options_display.keys()),
            horizontal=True
        )
        st.markdown("---")
        selected_key = demographic_chart_options_display[selected_demographic_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Content for this section will be added soon. Please provide new embed codes for Demographic charts.")


def render_economic_data_tab():
    """Renders the content for the Economic Data tab."""
    st.header("Economic Data")
    st.write("View economic indicators such as organic cotton certification status.")

    # This dictionary will be populated with new charts when you provide them.
    economic_chart_options_display = {
        # Example when you add a new economic chart:
        # "New Economic Chart Title": "new_economic_chart_key_from_DATAWRAPPER_EMBEDS",
    }

    if economic_chart_options_display:
        selected_economic_chart = st.radio(
            "Choose an economic chart to display:",
            list(economic_chart_options_display.keys()),
            horizontal=True
        )
        st.markdown("---")
        selected_key = economic_chart_options_display[selected_economic_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Content for this section will be added soon. Please provide new embed codes for Economic charts.")


def render_social_data_tab():
    """Renders the content for the Social Data tab."""
    st.header("Social Data")
    st.write("This section will cover parameters like labour register maintenance and participation in government schemes.")
    st.info("Content for this section will be added soon. Please provide new embed codes for Social charts.")

def render_environmental_data_tab():
    """Renders the content for the Environmental Data tab."""
    st.header("Environmental Data")
    st.write("This section presents data on crop residue management, irrigation sources, and organic cotton production.")

    # This dictionary will be populated with new charts when you provide them.
    environmental_chart_options_display = {
        # Example when you add a new environmental chart:
        # "New Environmental Chart Title": "new_environmental_chart_key_from_DATAWRAPPER_EMBEDS",
    }

    if environmental_chart_options_display:
        selected_environmental_chart = st.radio(
            "Choose an environmental chart to display:",
            list(environmental_chart_options_display.keys()),
            horizontal=True
        )
        st.markdown("---")
        selected_key = environmental_chart_options_display[selected_environmental_chart]
        display_datawrapper_embed(selected_key)
    else:
        st.info("Content for this section will be added soon. Please provide new embed codes for Environmental charts.")

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
