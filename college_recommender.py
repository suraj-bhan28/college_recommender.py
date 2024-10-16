import streamlit as st
import pandas as pd

# Updated dataset with specific colleges and cities
data = {
    'College': [
        'Poornima College Jaipur', 'SKIT College Jaipur', 
        'Lucknow College of Engineering', 'ND College Noida', 
        'GLA University Mathura', 'JCERC University Jaipur'
    ],
    'City': [
        'Jaipur', 'Jaipur', 
        'Lucknow', 'Noida', 
        'Mathura', 'Jaipur'
    ],
    'Courses_Offered': [
        'Engineering', 'Engineering', 
        'Engineering, Management', 'Engineering, IT', 
        'Engineering', 'Engineering'
    ],
    'Fees': [
        50000, 55000, 
        60000, 45000, 
        40000, 35000
    ],
    'Rank': [
        1, 2, 
        1, 3, 
        2, 4
    ],
    'JEE_Cutoff_Percentile': [
        90, 85, 
        88, 80, 
        75, 78  # Percentile required for admission
    ]
}

df = pd.DataFrame(data)

# Function to recommend colleges based on user input
def recommend_colleges(student_percentile):
    if student_percentile > 90:
        recommended = df[df['College'].isin(['SKIT College Jaipur', 'Lucknow College of Engineering'])]
    elif 75 <= student_percentile <= 90:
        recommended = df[df['College'] == 'Poornima College Jaipur']
    else:
        recommended = df[df['College'].isin(['ND College Noida', 'GLA University Mathura', 'JCERC University Jaipur'])]
    
    return recommended[['College', 'City', 'Fees', 'Rank', 'Courses_Offered', 'JEE_Cutoff_Percentile']]

# Streamlit interface for user input
st.title("College Recommender System")

# User input for JEE Main percentile
student_percentile = st.number_input("Enter your JEE Main Percentile:", min_value=0.0, max_value=100.0, value=85.0)

# If the user clicks the "Recommend" button
if st.button("Recommend Colleges"):
    # Get recommendations based on user input
    recommended_colleges = recommend_colleges(student_percentile)
    
    # Display the recommended colleges
    if recommended_colleges.empty:
        st.write("No colleges found matching your criteria.")
    else:
        st.write("Recommended Colleges:")
        st.dataframe(recommended_colleges)




