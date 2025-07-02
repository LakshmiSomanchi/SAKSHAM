import streamlit as st
import streamlit.components.v1 as components

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

    # Define the options for the radio buttons
    map_options = {
        "Map 1: Overview Distribution (Oq2xV)": {
            "code": """
            <div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
            """,
            "height": 650
        },
        "Map 2: Additional Regional View (dNfZU)": {
            "code": """
            <div style="min-height:384px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>
            """,
            "height": 450
        },
        "Map 3: Further Geographic Insight (7IEJR)": {
            "code": """
            <div style="min-height:677px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>
            """,
            "height": 730
        },
        "Map 4: Quick Geographic Detail (fNesy)": {
            "code": """
            <div style="min-height:114px" id="datawrapper-vis-fNesy"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/fNesy/embed.js" charset="utf-8" data-target="#datawrapper-vis-fNesy"></script><noscript><img src="https://datawrapper.dwcdn.net/fNesy/full.png" alt="" /></noscript></div>
            """,
            "height": 180
        },
        "Map 5: Detailed Geographic View (3Fewz)": {
            "code": """
            <div style="min-height:558px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>
            """,
            "height": 620
        },
    }

    # Create a radio button group for map selection
    # Using horizontal=True can make it more compact if many options
    selected_map_name = st.radio(
        "Choose a map to display:",
        list(map_options.keys()),
        horizontal=True # Display radio buttons horizontally
    )

    st.markdown("---") # Visual separator before the map

    # Display the selected map
    if selected_map_name: # Ensure a map is selected (it will be by default)
        map_info = map_options[selected_map_name]
        components.html(map_info["code"], height=map_info["height"], scrolling=False)
    else:
        st.info("Please select a map from the options above.")


# --- Content for 'Demographic Data' Tab ---
with tab_demographic:
    st.header("Demographic Data")
    st.write("This section will contain charts and graphs related to gender, age groups, and block/district-wise farmer distribution.")
    st.info("Content for this section will be added soon.")

# --- Content for 'Economic Data' Tab ---
with tab_economic:
    st.header("Economic Data")
    st.write("This section will display information about yield, certification status, and other economic indicators.")
    st.info("Content for this section will be added soon.")

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
