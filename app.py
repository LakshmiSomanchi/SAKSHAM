import streamlit as st
import streamlit.components.v1 as components

# --- Dashboard Title ---
st.title("SAKSHAM Baseline Survey Dashboard (Skeletal Structure)")
st.write("This dashboard currently features geographical overview maps.")

# --- Section 1: Geographic Data ---
st.header("Section 1: Geographic Data")

# First Datawrapper Map
st.subheader("Regional Overview Map 1")
datawrapper_embed_code_1 = """
<div style="min-height:598px" id="datawrapper-vis-Oq2xV"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/Oq2xV/embed.js" charset="utf-8" data-target="#datawrapper-vis-Oq2xV"></script><noscript><img src="https://datawrapper.dwcdn.net/Oq2xV/full.png" alt="" /></noscript></div>
"""
components.html(datawrapper_embed_code_1, height=600) # Set a height that makes the map visible

# Second Datawrapper Map
st.subheader("Regional Overview Map 2") # You can rename this subheader to be more specific
datawrapper_embed_code_2 = """
<div style="min-height:384px" id="datawrapper-vis-dNfZU"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/dNfZU/embed.js" charset="utf-8" data-target="#datawrapper-vis-dNfZU"></script><noscript><img src="https://datawrapper.dwcdn.net/dNfZU/full.png" alt="" /></noscript></div>
"""
components.html(datawrapper_embed_code_2, height=400) # Adjust height as needed for this map

# You can add more sections and charts here as you develop them.
# Example placeholder for future sections:
# st.header("Section 2: Demographic Data (Coming Soon!)")
# st.write("Charts for Gender, Adults and Children, and Block-wise distribution will appear here.")
