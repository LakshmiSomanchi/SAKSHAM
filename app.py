import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np # For generating sample data

# --- 0. Streamlit Page Configuration ---
st.set_page_config(
    page_title="SAKSHAM Project Comprehensive Dashboard",
    layout="wide", # Use a wide layout to maximize content space
    initial_sidebar_state="collapsed", # Keep the sidebar collapsed by default
    menu_items={
        'Get Help': 'https://www.google.com/search?q=SAKSHAM+project+help',
        'Report a bug': "https://github.com/your-username/your-repo/issues", # Replace with your actual repo
        'About': "# This is a comprehensive dashboard for the SAKSHAM Project, providing insights into demographic, economic, social, and environmental parameters."
    }
)

st.title("🌱 SAKSHAM Project: Comprehensive Dashboard")
st.markdown("---") # Visual separator

# --- Data Generation (Replace with your actual data loading) ---
# In a real application, you would load data from CSV, Excel, database, etc.
# Example:
# df_demographic = pd.read_csv("demographic_data.csv")
# df_economic = pd.read_excel("economic_data.xlsx")

# Sample Data Generation
np.random.seed(42) # for reproducibility

# Section 1: Demographic Data
gender_data = pd.DataFrame({
    'Category': ['Male', 'Female', 'Other'],
    'Count': [np.random.randint(4500, 5500), np.random.randint(4000, 5000), np.random.randint(50, 150)]
})

age_composition_data = pd.DataFrame({
    'Category': ['Adults (18+)', 'Children (0-17)'],
    'Count': [np.random.randint(7000, 8000), np.random.randint(2000, 3000)]
})

blocks = ['Block A', 'Block B', 'Block C', 'Block D', 'Block E']
districts = ['District X', 'District Y', 'District Z']
farmer_data = pd.DataFrame({
    'Block': np.random.choice(blocks, 1000, p=[0.2, 0.25, 0.15, 0.3, 0.1]),
    'District': np.random.choice(districts, 1000, p=[0.4, 0.3, 0.3])
})
# Aggregate farmer count by block and district
farmer_block_counts = farmer_data['Block'].value_counts().reset_index()
farmer_block_counts.columns = ['Block', 'Farmer Count']
farmer_district_counts = farmer_data['District'].value_counts().reset_index()
farmer_district_counts.columns = ['District', 'Farmer Count']


# Section 2: Economic Data
# Yield data (in Kg/acre)
yield_data = pd.DataFrame({
    'Yield (Kg/acre)': np.random.normal(loc=1500, scale=300, size=1000).clip(min=500, max=2500)
})

# Certification Status
certification_data = pd.DataFrame({
    'Status': ['Certified Organic', 'In Conversion', 'Conventional'],
    'Count': [np.random.randint(1500, 2000), np.random.randint(500, 800), np.random.randint(200, 400)]
})


# Section 3: Social Data
labour_register_data = pd.DataFrame({
    'Status': ['Registered', 'Not Registered'],
    'Count': [np.random.randint(800, 1200), np.random.randint(100, 300)]
})

govt_schemes_data = pd.DataFrame({
    'Scheme': ['PM-KISAN', 'Fasal Bima Yojana', 'Kisan Credit Card', 'Other Schemes', 'No Benefit'],
    'Beneficiaries': [np.random.randint(500, 700), np.random.randint(300, 500), np.random.randint(400, 600), np.random.randint(100, 200), np.random.randint(200, 400)]
})


# Section 4: Environmental Data
crop_residue_data = pd.DataFrame({
    'Management Method': ['Used as Fodder', 'Composted', 'Burned', 'Other'],
    'Count': [np.random.randint(600, 800), np.random.randint(300, 500), np.random.randint(50, 150), np.random.randint(20, 50)]
})

irrigation_source_data = pd.DataFrame({
    'Source': ['Borewell', 'Canal', 'River/Pond', 'Rainfed', 'Other'],
    'Farmers': [np.random.randint(800, 1200), np.random.randint(300, 600), np.random.randint(100, 300), np.random.randint(50, 150), np.random.randint(20, 50)]
})

num_irrigations_data = pd.DataFrame({
    'Number of Irrigations': np.random.choice([1, 2, 3, 4, 5, 6, 7], 1000, p=[0.05, 0.15, 0.25, 0.2, 0.15, 0.1, 0.1])
})
# Aggregate counts for bar graph
num_irrigations_counts = num_irrigations_data['Number of Irrigations'].value_counts().sort_index().reset_index()
num_irrigations_counts.columns = ['Number of Irrigations', 'Farmer Count']


# --- Dashboard Layout and Content ---

st.header("📊 Key Project Overviews")

# Create columns for KPIs
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
with kpi_col1:
    st.metric(label="Total Farmers Registered", value=f"{gender_data['Count'].sum() - gender_data.loc[gender_data['Category'] == 'Other', 'Count'].sum():,}") # Exclude 'Other' gender for farmer count
with kpi_col2:
    st.metric(label="Total Households Reached", value=f"{age_composition_data['Count'].sum() / 4:.0f}+") # Assuming avg 4 people per household for estimation
with kpi_col3:
    st.metric(label="Average Organic Yield (Kg/acre)", value=f"{yield_data['Yield (Kg/acre)'].mean():.0f} Kg")


st.markdown("---") # Separator

# --- Section 1: Demographic Data ---
st.header("Section 1: Demographic Data")
col1, col2 = st.columns(2) # Two columns for pie charts

with col1:
    st.subheader("Gender Distribution")
    fig_gender = px.pie(gender_data, names='Category', values='Count', title='Gender Composition',
                        hole=0.4, # Donut chart
                        color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_gender.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    st.subheader("Household Composition (Adults vs. Children)")
    fig_age_comp = px.pie(age_composition_data, names='Category', values='Count', title='Adults and Children',
                          hole=0.4,
                          color_discrete_sequence=px.colors.qualitative.Set2)
    fig_age_comp.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_age_comp, use_container_width=True)

st.subheader("Block-wise / District-wise Distribution of Farmers")
# Using tabs for Block vs District
tab_block, tab_district = st.tabs(["By Block", "By District"])

with tab_block:
    fig_block_farmers = px.bar(farmer_block_counts, x='Block', y='Farmer Count',
                               title='Farmer Distribution by Block',
                               color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_block_farmers, use_container_width=True)

with tab_district:
    fig_district_farmers = px.bar(farmer_district_counts, x='District', y='Farmer Count',
                                 title='Farmer Distribution by District',
                                 color_discrete_sequence=px.colors.qualitative.Vivid)
    st.plotly_chart(fig_district_farmers, use_container_width=True)

st.markdown("---")

# --- Section 2: Economic Data ---
st.header("Section 2: Economic Data")

# Bar Graph - Yield (create class intervals)
st.subheader("Yield Distribution (Kg/acre)")
# Define bins for yield
bins = [0, 800, 1200, 1600, 2000, 2500, np.inf]
labels = ['<800', '800-1200', '1201-1600', '1601-2000', '2001-2500', '>2500']
yield_data['Yield Interval'] = pd.cut(yield_data['Yield (Kg/acre)'], bins=bins, labels=labels, right=False)
yield_interval_counts = yield_data['Yield Interval'].value_counts().sort_index().reset_index()
yield_interval_counts.columns = ['Yield Interval', 'Count']

fig_yield = px.bar(yield_interval_counts, x='Yield Interval', y='Count',
                   title='Distribution of Cotton Yield (Kg/acre)',
                   color='Count', color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig_yield, use_container_width=True)

st.subheader("Certification Status")
fig_cert = px.pie(certification_data, names='Status', values='Count', title='Farmer Certification Status',
                  hole=0.4,
                  color_discrete_sequence=px.colors.qualitative.Safe)
fig_cert.update_traces(textposition='inside', textinfo='percent+label')
st.plotly_chart(fig_cert, use_container_width=True)

st.markdown("---")

# --- Section 3: Social Data ---
st.header("Section 3: Social Data")
col3, col4 = st.columns(2) # Two columns for pie charts

with col3:
    st.subheader("Labour Register Status")
    fig_labour = px.pie(labour_register_data, names='Status', values='Count', title='Farmers Registered in Labour Register',
                        hole=0.4,
                        color_discrete_sequence=px.colors.qualitative.T10)
    fig_labour.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_labour, use_container_width=True)

with col4:
    st.subheader("Government Schemes Benefited")
    fig_govt_schemes = px.pie(govt_schemes_data, names='Scheme', values='Beneficiaries', title='Beneficiaries of Government Schemes',
                              hole=0.4,
                              color_discrete_sequence=px.colors.qualitative.Dark2)
    fig_govt_schemes.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_govt_schemes, use_container_width=True)

st.markdown("---")

# --- Section 4: Environmental Data ---
st.header("Section 4: Environmental Data")
# Use st.columns for better layout if many bar graphs
env_col1, env_col2 = st.columns(2)

with env_col1:
    st.subheader("Crop Residue Management")
    fig_crop_residue = px.bar(crop_residue_data, x='Management Method', y='Count',
                              title='Crop Residue Management Methods',
                              color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig_crop_residue, use_container_width=True)

with env_col2:
    st.subheader("Source of Irrigation")
    fig_irrigation_source = px.bar(irrigation_source_data, x='Source', y='Farmers',
                                   title='Primary Irrigation Sources',
                                   color_discrete_sequence=px.colors.qualitative.Prism)
    st.plotly_chart(fig_irrigation_source, use_container_width=True)

st.subheader("Number of Irrigations Per Season")
fig_num_irrigations = px.bar(num_irrigations_counts, x='Number of Irrigations', y='Farmer Count',
                             title='Distribution of Number of Irrigations',
                             color='Farmer Count', color_continuous_scale=px.colors.sequential.Plasma)
st.plotly_chart(fig_num_irrigations, use_container_width=True)

st.markdown("---")
st.info(f"Dashboard Last Updated: {pd.Timestamp.now().strftime('%B %d, %Y %H:%M:%S')}") # Dynamic timestamp
st.markdown("Developed for SAKSHAM Project. For more information, contact your project lead.")
