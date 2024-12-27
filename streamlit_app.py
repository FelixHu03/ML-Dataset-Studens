import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Performance Analysis", page_icon="📚")

st.title("Student Performance Analysis")

try:
    # Load data csv 
    df = pd.read_csv("data/StudentPerformanceFactors.csv")
    
    # Basic stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        st.metric("Average Tutoring Sessions", round(df['Tutoring_Sessions'].mean(), 2))
    with col3:
        st.metric("Most Common Education", df['Parental_Education_Level'].mode()[0])

    # Tutoring Sessions
    st.header("Tutoring Sessions Analysis")
    fig_tutoring = px.line(
        df.reset_index(), 
        x='siswa(1-n)', 
        y='Tutoring_Sessions',
        title="Tutoring Sessions Distribution"
    )
    st.plotly_chart(fig_tutoring)

    # Parental Education
    st.header("Parental Education Distribution")
    parental_counts = df['Parental_Education_Level'].value_counts()
    fig_parent = px.pie(
        values=parental_counts.values,
        names=parental_counts.index
    )
    st.plotly_chart(fig_parent)

    # Gender Distribution
    st.header("Gender Distribution")
    gender_counts = df['Gender'].value_counts()
    fig_gender = px.bar(
        x=gender_counts.index,
        y=gender_counts.values,
        labels={'x': 'Gender', 'y': 'Count'}
    )
    st.plotly_chart(fig_gender)

    # Raw Data
    if st.checkbox("Show Raw Data"):
        st.dataframe(df)

except Exception as e:
    st.error(f"Error reading data: {str(e)}")

st.markdown("---")
st.caption("Created by Felix")