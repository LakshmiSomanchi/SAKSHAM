import streamlit as st
# Import the components module for embedding HTML
import streamlit.components.v1 as components

# --- Dashboard Title ---
st.title("SAKSHAM Baseline Dashboard")
st.write("This dashboard currently features a geographical overview map.")

# --- Section 1: Geographic Data (for the map) ---
st.header("Geographic Data")
st.subheader("Regional Overview Map")

# Datawrapper embed code as a string
datawrapper_embed_code = """
<div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
"""

# Embed the HTML using st.components.v1.html
components.html(datawrapper_embed_code, height=600) # Set a height that makes the map visible

# You can add more sections and charts here as you develop them.
# Example placeholder for future sections:
# st.header("Section 2: Demographic Data (Coming Soon!)")
# st.write("Charts for Gender, Adults and Children, and Block-wise distribution will appear here.")

# st.header("Section 3: Economic Data (Coming Soon!)")
# st.write("Charts for Yield and Certification Status will appear here.")
