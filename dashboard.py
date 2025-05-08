import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('dashboard.csv')

# Title of the dashboard
st.title("Prediction Dashboard")

# Sidebar input for Agent ID
st.sidebar.header("Agent ID")
agent_code = st.sidebar.text_input("Enter the Agent Code")

# Filter and display data based on the entered Agent Code
if agent_code:
    # Filter the dataframe for the entered Agent Code
    filtered_data = df[df['agent_code'] == agent_code]
    
    if not filtered_data.empty:
        # Display filtered data
        st.header(f"Predictions for Agent: {agent_code}")
        st.dataframe(filtered_data[['target_column']])  # Replace 'target_column' with the actual column name
    else:
        st.warning("No data found for the entered Agent Code.")
else:
    st.info("Please enter an Agent Code to view predictions.")