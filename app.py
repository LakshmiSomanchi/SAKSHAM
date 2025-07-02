import streamlit as st
import streamlit.components.v1 as components
import os

# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Dashboard",
    layout="wide", # Use a wide layout to maximize space for the dashboard
    initial_sidebar_state="collapsed", # Keep the sidebar collapsed by default
    menu_items={
        'Get Help': 'https://www.google.com/search?q=streamlit+help', # Example help link
        'Report a bug': "https://www.google.com/search?q=streamlit+report+bug", # Example bug report link
        'About': "# This is a dashboard for the SAKSHAM Project."
    }
)

# --- Read and Embed HTML ---
# Get the directory of the current script
current_dir = os.path.dirname(__file__)
html_file_path = os.path.join(current_dir, "index.html")

try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error(f"Error: HTML file not found at {html_file_path}. Please ensure 'index.html' is in the same directory as 'streamlit_app.py'.")
    html_content = "<h1>Dashboard content could not be loaded.</h1>"

# The height parameter is crucial. You'll need to adjust this value
# to ensure your entire dashboard is visible without excessive scrolling.
# A value around 1200-1800 is a good starting point, but it depends
# on the total height of your HTML content, especially the Datawrapper embeds.
# You can open index.html in your browser, inspect element, and get an idea of the total height.
# Or, start with a generous height and adjust down.
components.html(html_content, height=1800, scrolling=True) # Set scrolling to True if content might exceed height
