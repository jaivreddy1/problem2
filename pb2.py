import pandas as pd
import streamlit as st

# Load data
df_university = pd.read_csv('/content/university_student_dashboard_data.csv')

def university_dashboard():
    st.title("University Admissions & Satisfaction Dashboard")

    # Total Applications and Enrollments per Term
    st.write("### Total Applications and Enrollments per Term")
    term_summary = df_university.groupby('term')[['applications', 'enrollments']].sum()
    st.bar_chart(term_summary)

    # Retention Rate Over Time
    st.write("### Retention Rate Over Time")
    retention_trend = df_university.groupby('year')['retention_rate'].mean()
    st.line_chart(retention_trend)

    # Student Satisfaction Scores
    st.write("### Student Satisfaction Scores")
    satisfaction_trend = df_university.groupby('year')['satisfaction_score'].mean()
    st.line_chart(satisfaction_trend)

    # Enrollment Breakdown by Department
    st.write("### Enrollment Breakdown by Department")
    department_enrollment = df_university.groupby('department')['enrollments'].sum()
    st.bar_chart(department_enrollment)

    # Comparison Between Spring and Fall Terms
    st.write("### Comparison Between Spring and Fall Terms")
    term_comparison = df_university.groupby('term')[['applications', 'enrollments']].mean()
    st.bar_chart(term_comparison)

# Run the dashboard function
university_dashboard()
