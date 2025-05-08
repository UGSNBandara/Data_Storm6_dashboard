import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dashboard.csv')

st.title("Prediction Dashboard - September 2024")

st.sidebar.header("Agent ID")
agent_code = st.sidebar.text_input("Enter the Agent Code")

def get_recommendation(category):
    recommendations = {
        'Motivated & Policy Growth': (
            "Sustain momentum by identifying key factors driving both motivation and policy success. "
            "Incorporate these best practices into team-wide training programs. Assign this agent as a mentor "
            "for underperforming agents to replicate success."
        ),
        'Motivated & Policy Decline': (
            "Analyze why policy numbers are declining despite high motivation. Conduct one-on-one reviews to identify "
            "potential barriers such as operational inefficiencies or misaligned targets. Develop a tailored improvement plan, "
            "and provide tools or resources to regain policy growth."
        ),
        'Low Motivation & Policy Growth': (
            "Identify the external drivers behind policy growth and ensure they are sustainable. At the same time, address the root causes "
            "of low motivation through personalized coaching, recognition programs, or career development opportunities. "
            "Consider workload adjustments or resource allocation to boost morale."
        ),
        'Low Motivation & Policy Decline': (
            "This requires immediate intervention. Conduct a thorough diagnostic assessment to determine whether issues stem from "
            "leadership, training gaps, or external pressures. Implement targeted training programs, performance incentives, "
            "and regular check-ins to rebuild confidence and drive. Pair the agent with a high-performing peer for on-the-job support."
        )
    }
    return recommendations.get(category, "No recommendation available.")

if agent_code:
    filtered_data = df[df['agent_code'] == agent_code]
    
    if not filtered_data.empty:
        st.header(f"Predictions and Analysis for Agent: {agent_code}")
        
        st.subheader("Predicted Risk of Next Month")
        for category in filtered_data['target_column'].unique():
            if category == 1:
                st.write("No Risk")
            else:
                st.write("At Risk")
        
        st.subheader("Category")
        st.dataframe(filtered_data[['combined_category']])
        
        st.subheader("Stratergies")
        for category in filtered_data['combined_category'].unique():
            st.write(get_recommendation(category))
        
    else:
        st.warning("No data found for the entered Agent Code.")
else:
    st.info("Please enter an Agent Code to view predictions.")


st.subheader("Category Distribution")
category_counts = df['combined_category'].value_counts()
        
fig, ax = plt.subplots()
category_counts.plot(kind='bar', color=['green', 'orange', 'purple', 'red'], ax=ax)
ax.set_title("Category Distribution for Selected Agent")
ax.set_xlabel("Category")
ax.set_ylabel("Count")
st.pyplot(fig)