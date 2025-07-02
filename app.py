import streamlit as st
import streamlit.components.v1 as components
import os
import datetime # Import datetime for dynamic timestamp

# --- 0. Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide", # Use a wide layout to maximize space for the dashboard
    initial_sidebar_state="collapsed", # Keep the sidebar collapsed by default for a full dashboard view
    menu_items={
        'Get Help': 'https://www.google.com/search?q=saksham+project+support', # More relevant help link
        'Report a bug': "https://github.com/your-username/your-repo-name/issues", # Suggest linking to a real GitHub issues page
        'About': "# SAKSHAM Project Dashboard\nThis dashboard provides an comprehensive overview of key metrics for the SAKSHAM Cotton Project. Visualizations are sourced directly from Datawrapper embeds within the core HTML structure."
    }
)

# --- 1. Dashboard Header in Streamlit ---
# This appears *above* your embedded HTML
st.title("🌱 SAKSHAM Project: Interactive Dashboard")
st.markdown("""
Welcome to the comprehensive dashboard for the SAKSHAM Cotton Project.
This interface brings together key insights across various parameters, leveraging interactive visualizations from Datawrapper.
""")
st.markdown("---") # Visual separator


# --- 2. Streamlit Sidebar (Optional) ---
# This is a good place for controls, filters, or additional info if your dashboard grows
with st.sidebar:
    st.header("Dashboard Controls")
    st.info("This sidebar can be used for filters, navigation, or additional information.")
    st.markdown("---")
    st.markdown("Developed by the SAKSHAM Project Team.")
    st.caption(f"App deployed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %Z')}")


# --- 3. Read and Embed HTML Content ---
current_dir = os.path.dirname(__file__)
html_file_path = os.path.join(current_dir, "SAKSHAM.html")

# Define a default or estimated height. This is crucial for the embedded HTML.
# You will likely need to adjust this value after initial deployment.
# TIP: Open your index.html in a browser, use developer tools to inspect the <body> or .dashboard-container
# and find its computed height, then add a little buffer.
# For example, if the HTML content is 1750px tall, set height=1800.
DEFAULT_EMBED_HEIGHT = 1800 # A good starting point, adjust as needed

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Embed the HTML content
    # scrolling=True allows the iframe itself to have scrollbars if its content exceeds 'height'
    # It's often better to let the main Streamlit page handle scrolling if possible,
    # so consider making 'height' large enough to fit all content.
    components.html(html_content, height=DEFAULT_EMBED_HEIGHT, scrolling=True)

except FileNotFoundError:
    st.error(f"""
        **Dashboard HTML file not found!**
        Please ensure that `index.html` is located in the same directory as `streamlit_app.py`.
        Current expected path: `{html_file_path}`
        If you are running this locally, verify the file path.
        If deploying to Streamlit Cloud, ensure both files are pushed to your GitHub repository.
    """)
    # Optionally, provide a placeholder for a missing dashboard
    st.image("https://via.placeholder.com/800x400.png?text=Dashboard+Loading+Error", use_column_width=True)
    st.warning("The dashboard cannot be displayed without the `SAKSHAM.html` file.")

# --- 4. Streamlit Footer ---
# This appears *below* your embedded HTML
st.markdown("---")
st.markdown(f"**Data last updated as of:** {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
st.markdown("For any queries or more detailed information, please contact the SAKSHAM Project team.")
