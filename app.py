import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- Dashboard Title ---
st.title("SAKSHAM Baseline Survey Dashboard (Skeletal Structure)")
st.write("This dashboard provides a skeletal structure with dummy data for select parameters from the baseline survey.")

# --- Section 1: Demographic Data ---
st.header("Section 1: Demographic Data")

# Parameter: Gender (Pie Chart)
st.subheader("Gender Distribution")
gender_data = pd.DataFrame({'Category': ['Male', 'Female', 'Other'], 'Count': [np.random.randint(50, 150), np.random.randint(50, 150), np.random.randint(5, 20)]})
fig_gender = px.pie(gender_data, values='Count', names='Category', title='Gender Distribution of Farmers')
st.plotly_chart(fig_gender)

# Parameter: Adults and Children (Pie Chart)
st.subheader("Adults vs. Children")
age_group_data = pd.DataFrame({'Category': ['Adults', 'Children'], 'Count': [np.random.randint(200, 500), np.random.randint(50, 200)]})
fig_age_group = px.pie(age_group_data, values='Count', names='Category', title='Adults and Children in Households')
st.plotly_chart(fig_age_group)

# Parameter: Block-wise / district-wise distribution of farmers (Bar Graph)
st.subheader("Block/District-wise Distribution of Farmers")
blocks = [f'Block {chr(65 + i)}' for i in range(5)] # Example blocks A, B, C, D, E
block_data = pd.DataFrame({'Block': blocks, 'Number of Farmers': np.random.randint(100, 400, size=len(blocks))})
fig_block = px.bar(block_data, x='Block', y='Number of Farmers', title='Distribution of Farmers by Block')
st.plotly_chart(fig_block)

# --- Section 2: Economic ---
st.header("Section 2: Economic")

# Parameter: Yield (Bar Graph - create class intervals)
st.subheader("Yield Distribution (Class Intervals)")
yield_data = pd.DataFrame({
    'Yield Class': ['0-100 kg', '101-200 kg', '201-300 kg', '301-400 kg', '400+ kg'],
    'Number of Farmers': np.random.randint(20, 100, size=5)
})
fig_yield = px.bar(yield_data, x='Yield Class', y='Number of Farmers', title='Distribution of Farmers by Yield Class')
st.plotly_chart(fig_yield)

# Parameter: Certification Status (Pie Chart)
st.subheader("Certification Status")
certification_data = pd.DataFrame({'Status': ['Certified', 'Not Certified', 'In Progress'], 'Count': [np.random.randint(30, 80), np.random.randint(80, 150), np.random.randint(10, 30)]})
fig_certification = px.pie(certification_data, values='Count', names='Status', title='Farmer Certification Status')
st.plotly_chart(fig_certification)

# --- Section 3: Social ---
st.header("Section 3: Social")

# Parameter: Labour Register (Pie Chart)
st.subheader("Labour Register Status")
labour_register_data = pd.DataFrame({'Status': ['Maintained', 'Not Maintained'], 'Count': [np.random.randint(70, 120), np.random.randint(30, 80)]})
fig_labour_register = px.pie(labour_register_data, values='Count', names='Status', title='Maintenance of Labour Register')
st.plotly_chart(fig_labour_register)

# Parameter: Govt. Schemes (Pie Chart)
st.subheader("Participation in Government Schemes")
gov_schemes_data = pd.DataFrame({'Status': ['Participating', 'Not Participating'], 'Count': [np.random.randint(100, 200), np.random.randint(50, 100)]})
fig_gov_schemes = px.pie(gov_schemes_data, values='Count', names='Status', title='Farmer Participation in Government Schemes')
st.plotly_chart(fig_gov_schemes)

# --- Section 4: Environmental ---
st.header("Section 4: Environmental")

# Parameter: Crop Residue (Bar Graph)
st.subheader("Crop Residue Management")
crop_residue_data = pd.DataFrame({
    'Management Method': ['Burned', 'Composted', 'Incorporated into Soil', 'Used as Fodder'],
    'Number of Farmers': np.random.randint(20, 80, size=4)
})
fig_crop_residue = px.bar(crop_residue_data, x='Management Method', y='Number of Farmers', title='Crop Residue Management Practices')
st.plotly_chart(fig_crop_residue)

# Parameter: Irrigation Source (Bar Graph)
st.subheader("Primary Irrigation Source")
irrigation_source_data = pd.DataFrame({
    'Source': ['Borewell', 'Canal', 'River', 'Pond', 'Rainfed'],
    'Number of Farmers': np.random.randint(30, 100, size=5)
})
fig_irrigation_source = px.bar(irrigation_source_data, x='Source', y='Number of Farmers', title='Primary Irrigation Source of Farmers')
st.plotly_chart(fig_irrigation_source)

# Parameter: No. of Irrigations (Bar Graph)
st.subheader("Number of Irrigations per Season")
num_irrigations_data = pd.DataFrame({
    'Number of Irrigations': ['0-1', '2-3', '4-5', '6+'],
    'Number of Farmers': np.random.randint(40, 120, size=4)
})
fig_num_irrigations = px.bar(num_irrigations_data, x='Number of Irrigations', y='Number of Farmers', title='Number of Irrigations Applied per Season')
st.plotly_chart(fig_num_irrigations)
