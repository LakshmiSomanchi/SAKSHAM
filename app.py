import streamlit as st
import streamlit.components.v1 as components
import pandas as pd # Used only for the dynamic timestamp, but keeping if you add other pandas logic later

# --- 0. Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard - Datawrapper Embeds",
    layout="wide", # Use a wide layout to maximize content space
    initial_sidebar_state="collapsed", # Keep the sidebar collapsed by default
    menu_items={
        'Get Help': 'https://www.google.com/search?q=datawrapper+streamlit+help',
        'Report a bug': "https://github.com/your-username/your-repo/issues", # Replace with your actual repo if you create one
        'About': "# This dashboard for the SAKSHAM Project embeds interactive charts directly from Datawrapper."
    }
)

st.title("🌱 SAKSHAM Project: Dashboard with Datawrapper Visualizations")
st.markdown("---") # Visual separator

# --- Datawrapper Embed Codes (as Python strings) ---
# It's best to define these as multi-line strings for clarity.
# You provided these earlier.

DATAWRAPPER_LOCATIONS = """
<div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
"""

DATAWRAPPER_HOUSEHOLD_COMPOSITION = """
<div style="min-height:451px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>
"""

DATAWRAPPER_GENDER_RATIO = """
<div style="min-height:114px" id="datawrapper-vis-fNesy"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/fNesy/embed.js" charset="utf-8" data-target="#datawrapper-vis-fNesy"></script><noscript><img src="https://datawrapper.dwcdn.net/fNesy/full.png" alt="" /></noscript></div>
"""

DATAWRAPPER_IRRIGATION_SOURCE = """
<div style="min-height:258px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>
"""

DATAWRAPPER_AVG_PRODUCTION = """
<div style="min-height:468px" id="datawrapper-vis-3Fewz"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/3Fewz/embed.js" charset="utf-8" data-target="#datawrapper-vis-3Fewz"></script><noscript><img src="https://datawrapper.dwcdn.net/3Fewz/full.png" alt="" /></noscript></div>
"""

# --- Dashboard Layout and Content ---

st.header("📊 Key Project Overviews (Placeholder KPIs)")
st.info("Note: These KPIs are static placeholders. For dynamic KPIs, you would need to connect to your raw data.")

# Create columns for KPIs
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
with kpi_col1:
    st.metric(label="Total Locations Covered", value="50+")
with kpi_col2:
    st.metric(label="Estimated Households Reached", value="2,500+")
with kpi_col3:
    st.metric(label="Avg. Organic Yield (Kg/acre)", value="1,500 Kg")


st.markdown("---") # Separator

# --- Section 1: Demographic Data ---
st.header("Section 1: Demographic Data")
st.markdown("This section provides an overview of the population and geographical distribution within the SAKSHAM project.")

col1, col2 = st.columns(2) # Two columns for charts

with col1:
    st.subheader("Gender Ratio")
    # Using the exact min-height from Datawrapper, but allowing Streamlit to manage iframe height
    # The 'height' parameter in components.html is crucial to avoid cut-offs.
    components.html(DATAWRAPPER_GENDER_RATIO, height=150, scrolling=False) # Gender ratio is small, adjust height accordingly

with col2:
    st.subheader("Household Composition")
    components.html(DATAWRAPPER_HOUSEHOLD_COMPOSITION, height=480, scrolling=False) # Adjust height based on actual content

st.subheader("SAKSHAM Locations Map")
# This chart is usually large, so give it full width and sufficient height
components.html(DATAWRAPPER_LOCATIONS, height=620, scrolling=False) # Adjust height based on actual content

st.markdown("---")

# --- Section 2: Economic Data ---
st.header("Section 2: Economic Data")
st.markdown("Insights into agricultural economics and farmer certification status.")

st.subheader("Average Production of Organic Cotton/Acre/Kg")
# This chart is also substantial
components.html(DATAWRAPPER_AVG_PRODUCTION, height=500, scrolling=False) # Adjust height

st.subheader("Certification Status (Placeholder Chart)")
st.info("Please provide Datawrapper embed code for 'Certification Status'. This is a placeholder.")
# If you create a Datawrapper chart for certification status, you'd add it here:
# components.html(DATAWRAPPER_CERTIFICATION_STATUS, height=HEIGHT_FOR_CERT_CHART, scrolling=False)

st.markdown("---")

# --- Section 3: Social Data ---
st.header("Section 3: Social Data")
st.markdown("Information on social welfare and community engagement.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Labour Register (Placeholder Chart)")
    st.info("Please provide Datawrapper embed code for 'Labour Register'. This is a placeholder.")
    # components.html(DATAWRAPPER_LABOUR_REGISTER, height=HEIGHT_FOR_LABOUR_CHART, scrolling=False)

with col4:
    st.subheader("Govt. Schemes (Placeholder Chart)")
    st.info("Please provide Datawrapper embed code for 'Govt. Schemes'. This is a placeholder.")
    # components.html(DATAWRAPPER_GOVT_SCHEMES, height=HEIGHT_FOR_GOVT_SCHEMES_CHART, scrolling=False)

st.markdown("---")

# --- Section 4: Environmental Data ---
st.header("Section 4: Environmental Data")
st.markdown("Environmental impact and agricultural practices.")

st.subheader("Source of Irrigation")
components.html(DATAWRAPPER_IRRIGATION_SOURCE, height=280, scrolling=False) # Adjust height

st.subheader("Crop Residue (Placeholder Chart)")
st.info("Please provide Datawrapper embed code for 'Crop Residue'. This is a placeholder.")
# components.html(DATAWRAPPER_CROP_RESIDUE, height=HEIGHT_FOR_CROP_RESIDUE_CHART, scrolling=False)

st.subheader("No. of Irrigations (Placeholder Chart)")
st.info("Please provide Datawrapper embed code for 'No. of Irrigations'. This is a placeholder.")
# components.html(DATAWRAPPER_NO_OF_IRRIGATIONS, height=HEIGHT_FOR_IRRIGATIONS_CHART, scrolling=False)

st.markdown("---")
st.info(f"Dashboard Last Updated: {pd.Timestamp.now().strftime('%B %d, %Y at %I:%M:%S %p %Z')}") # Dynamic timestamp
st.markdown("Developed for SAKSHAM Project. For more information, contact your project lead.")
