import streamlit as st
import streamlit.components.v1 as components

# --- Page Configuration (MUST be the first Streamlit command) ---
st.set_page_config(
    page_title="SAKSHAM Baseline Survey Dashboard",
    page_icon="🌍", # You can choose a relevant emoji icon
    layout="wide", # Use the full width of the browser
    initial_sidebar_state="expanded" # Keep sidebar open by default
)

# --- Dashboard Title ---
st.title("📊 SAKSHAM Baseline Survey Dashboard") # Added an emoji
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
    st.write("Explore the regional distribution and characteristics through these interactive maps.")

    # You can use columns to place maps side-by-side if they are small enough
    # For now, let's stack them as they have considerable height

    st.subheader("Map 1: Overview Distribution")
    datawrapper_embed_code_1 = """
    <div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
    """
    components.html(datawrapper_embed_code_1, height=600, scrolling=True) # Added scrolling=True

    st.markdown("---") # Visual separator

    st.subheader("Map 2: Additional Regional View")
    datawrapper_embed_code_2 = """
    <div style="min-height:384px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>
    """
    components.html(datawrapper_embed_code_2, height=400, scrolling=True) # Added scrolling=True

    st.markdown("---") # Visual separator

    st.subheader("Map 3: Further Geographic Insight")
    datawrapper_embed_code_3 = """
    <div style="min-height:677px" id="datawrapper-vis-7IEJR"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/7IEJR/embed.js" charset="utf-8" data-target="#datawrapper-vis-7IEJR"></script><noscript><img src="https://datawrapper.dwcdn.net/7IEJR/full.png" alt="" /></noscript></div>
    """
    components.html(datawrapper_embed_code_3, height=700, scrolling=True) # Adjusted height and added scrolling=True


# --- Content for 'Demographic Data' Tab ---
with tab_demographic:
    st.header("Demographic Data")
    st.write("This section will contain charts and graphs related to gender, age groups, and block/district-wise farmer distribution.")
    st.info("Content for this section will be added soon.") # Placeholder message

    # Example of how you would add a chart here in the future:
    # st.subheader("Gender Distribution (Placeholder)")
    # gender_data = pd.DataFrame({'Category': ['Male', 'Female'], 'Count': [100, 80]})
    # fig_gender = px.pie(gender_data, values='Count', names='Category')
    # st.plotly_chart(fig_gender)


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
