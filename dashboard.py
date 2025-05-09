import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dashboard.csv')

# Add custom CSS for modern styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    h1 {
        color: #90CAF9;
        font-size: 2.5rem;
        font-weight: 700;
    }
    h2 {
        color: #64B5F6;
        font-size: 1.8rem;
        font-weight: 600;
    }
    h3 {
        color: #42A5F5;
        font-size: 1.5rem;
        font-weight: 500;
    }
    .stButton button {
        background-color: #1E88E5;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        font-weight: 500;
    }
    .stButton button:hover {
        background-color: #1565C0;
    }
    .stTextInput input {
        border-radius: 5px;
        border: 1px solid #BDBDBD;
    }
    .stTextInput input:focus {
        border-color: #1E88E5;
    }
    .stDataFrame {
        border-radius: 5px;
        border: 1px solid #E0E0E0;
    }
    .stWarning {
        background-color: #FFF3E0;
        color: #E65100;
        padding: 1rem;
        border-radius: 5px;
    }
    .stInfo {
        background-color: #E3F2FD;
        color: #0D47A1;
        padding: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Update the title with modern styling
st.title("Prediction Dashboard - September 2024")

# Update the sidebar header with modern styling
st.sidebar.markdown("<h2 style='color: #90CAF9;'>Agent ID</h2>", unsafe_allow_html=True)
agent_code = st.sidebar.text_input("Enter the Agent Code")

def get_recommendation(category):
    recommendations = {
        'Motivated & Policy Growth': {
            "Provide incentives such as bonuses, promotions, or recognition to maintain their motivation.",
            "Offer challenging projects or roles to further enhance their skills and growth trajectory.",
            "Encourage mentoring opportunities to share their knowledge and inspire others.",
            "Give constructive feedback and appreciation to reinforce positive behaviors.",
        },
        'Motivated & Policy Decline': {
            "Conduct one-on-one meetings to identify reasons for the decline (e.g., workload, external stressors).",
            "Offer refresher training to address any emerging skill gaps.",
            "Ensure tasks are well-distributed and aligned with their strengths.",
            "Provide motivational talks or stress management sessions to re-ignite their enthusiasm.",
        },
        'Low Motivation & Policy Growth': {
            "Introduce gamification or team challenges to increase enthusiasm.",
            "Foster a collaborative workspace with opportunities for peer interaction and feedback.",
            "Acknowledge and reward their progress to boost morale.",
            "Offer targeted workshops to increase confidence and align their abilities with their tasks.",
        },
        'Low Motivation & Policy Decline': {
            "Conduct detailed discussions to understand underlying issues (e.g., personal, professional, or environmental).",
            "Provide personalized coaching or mentorship to address specific challenges.",
            "Reassess and reassign tasks to match their capabilities and interests.",
            "Schedule regular check-ins to track improvements and adjust interventions as needed.",
            "Organize activities like team-building events, motivational sessions, or role rotations to reignite their interest.",
        }
    }
    return recommendations.get(category, "No recommendation available.")

if agent_code:
    filtered_data = df[df['agent_code'] == agent_code]
    
    if not filtered_data.empty:
        st.markdown("<h2 style='color: #64B5F6;'>Agent : " + agent_code + "</h2>", unsafe_allow_html=True)
        
        st.markdown("<h3 style='color: #42A5F5;'>Predicted Risk of Next Month</h3>", unsafe_allow_html=True)
        for category in filtered_data['target_column'].unique():
            if category == 1:
                st.markdown("<p style='color: #81C784;'>No Risk</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color: #E57373;'>At Risk</p>", unsafe_allow_html=True)
        
        
        st.markdown("<h3 style='color: #42A5F5;'>Category</h3>", unsafe_allow_html=True)
        st.write(filtered_data['combined_category'].unique())
        
        st.markdown("<h3 style='color: #42A5F5;'>Strategies</h3>", unsafe_allow_html=True)
        for category in filtered_data['combined_category'].unique():
            strategies = get_recommendation(category)
            for s in strategies:
                st.markdown("<p style='color: #E0E0E0;'>• " + s + "</p>", unsafe_allow_html=True)
        
    else:
        st.warning("No data found for the entered Agent Code.")
else:
    st.info("Please enter an Agent Code to view predictions.")



st.markdown("<h3 style='color: #42A5F5;'>Category Distribution</h3>", unsafe_allow_html=True)
category_counts = df['combined_category'].value_counts()

fig, ax = plt.subplots(facecolor='#0E1117')
colors = ['#90CAF9', '#81C784', '#FFB74D', '#E57373']
category_counts.plot(kind='bar', color=colors, ax=ax)
ax.set_title("Category Distribution for Selected Agent", fontsize=14, fontweight='bold', color='#90CAF9')
ax.set_xlabel("Category", fontsize=12, color='#E0E0E0')
ax.set_ylabel("Count", fontsize=12, color='#E0E0E0')
ax.tick_params(axis='both', colors='#E0E0E0')
ax.set_facecolor('#0E1117')
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("<h3 style='color: #42A5F5;'>Risk Distribution</h3>", unsafe_allow_html=True)
target_counts = df['target_column'].value_counts()
fig_pie, ax_pie = plt.subplots(facecolor='#0E1117')
colors_pie = ['#81C784', '#E57373']  # Green for No Risk, Red for At Risk
labels = ['No Risk' if x == 1 else 'At Risk' for x in target_counts.index]
ax_pie.pie(target_counts, labels=labels, colors=colors_pie, autopct='%1.1f%%', textprops={'color': '#E0E0E0'})
ax_pie.set_title('Risk Distribution', color='#90CAF9', pad=20)
st.pyplot(fig_pie)
