import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page config
st.set_page_config(
    page_title="Student Performance Analysis",
    page_icon="📚",
    layout="wide"
)

# Title and description
st.title("📚 Student Performance Analysis Dashboard")
st.markdown("Analysis of student performance factors including tutoring sessions, parental education, and gender distribution.")

# Data loading
@st.cache_data
def load_data():
    df = pd.read_csv("StudentPerformanceFactors.csv")
    return df

try:
    df = load_data()
    
    # Main metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Students", len(df))
    with col2:
        st.metric("Average Tutoring Sessions", round(df['Tutoring_Sessions'].mean(), 2))
    with col3:
        st.metric("Most Common Parent Education", df['Parental_Education_Level'].mode()[0])

    # Tutoring Sessions Analysis
    st.header("📊 Tutoring Sessions Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        fig_tutoring = px.line(
            df.reset_index(), 
            x='index', 
            y='Tutoring_Sessions',
            title="Tutoring Sessions per Student"
        )
        fig_tutoring.update_layout(xaxis_title="Student Index", yaxis_title="Number of Sessions")
        st.plotly_chart(fig_tutoring, use_container_width=True)
    
    with col2:
        tutoring_stats = pd.DataFrame({
            'Statistic': ['Mean', 'Median', 'Max', 'Min'],
            'Value': [
                df['Tutoring_Sessions'].mean(),
                df['Tutoring_Sessions'].median(),
                df['Tutoring_Sessions'].max(),
                df['Tutoring_Sessions'].min()
            ]
        })
        st.dataframe(tutoring_stats, use_container_width=True)

    # Parental Education Analysis
    st.header("👨‍👩‍👧‍👦 Parental Education Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        parental_counts = df['Parental_Education_Level'].value_counts()
        fig_parent = px.pie(
            values=parental_counts.values,
            names=parental_counts.index,
            title="Distribution of Parental Education Levels"
        )
        st.plotly_chart(fig_parent, use_container_width=True)
    
    with col2:
        st.dataframe(
            df['Parental_Education_Level'].value_counts().reset_index().rename(
                columns={'index': 'Education Level', 'Parental_Education_Level': 'Count'}
            ),
            use_container_width=True
        )

    # Gender Analysis
    st.header("⚤ Gender Distribution")
    col1, col2 = st.columns(2)
    
    with col1:
        gender_counts = df['Gender'].value_counts()
        fig_gender = px.bar(
            x=gender_counts.index,
            y=gender_counts.values,
            title="Gender Distribution",
            labels={'x': 'Gender', 'y': 'Count'}
        )
        st.plotly_chart(fig_gender, use_container_width=True)
    
    with col2:
        st.dataframe(
            df['Gender'].value_counts().reset_index().rename(
                columns={'index': 'Gender', 'Gender': 'Count'}
            ),
            use_container_width=True
        )

    # Additional Analysis
    st.header("🔍 Cross Analysis")
    fig_box = px.box(
        df,
        x="Parental_Education_Level",
        y="Tutoring_Sessions",
        color="Gender",
        title="Tutoring Sessions by Parental Education and Gender"
    )
    st.plotly_chart(fig_box, use_container_width=True)

    # Raw Data
    if st.checkbox("Show Raw Data"):
        st.dataframe(df)

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please ensure the CSV file is in the same directory as the script.")

# Footer
st.markdown("---")
st.markdown("Created by Felix")