import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
def load_data():
    file_path = "university_student_dashboard_data.csv"
    df = pd.read_csv(file_path)
    return df

df = load_data()

# Streamlit app
st.title("University Admissions and Student Satisfaction Dashboard")

# Filters
years = df['Year'].unique()
selected_year = st.selectbox("Select Year", years)

df_filtered = df[df['Year'] == selected_year]

# Applications, Admissions, and Enrollments over time
st.subheader("Applications, Admissions, and Enrollments")
fig, ax = plt.subplots()
ax.plot(df_filtered['Term'], df_filtered['Applications'], label='Applications', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Admitted'], label='Admitted', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Enrolled'], label='Enrolled', marker='o')
ax.set_ylabel("Count")
ax.set_title("Admissions Trends")
ax.legend()
st.pyplot(fig)

# Retention and Satisfaction Trends
st.subheader("Retention Rate and Student Satisfaction")
fig, ax = plt.subplots()
ax.plot(df_filtered['Term'], df_filtered['Retention Rate (%)'], label='Retention Rate', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Student Satisfaction (%)'], label='Satisfaction', marker='o')
ax.set_ylabel("Percentage")
ax.set_title("Retention and Satisfaction Trends")
ax.legend()
st.pyplot(fig)

# Enrollment Breakdown by Department
st.subheader("Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()
fig, ax = plt.subplots()
ax.bar(departments, department_counts)
ax.set_ylabel("Number of Students")
ax.set_title("Department-wise Enrollment")
st.pyplot(fig)

# Insights and Summary
st.subheader("Key Insights")
insights = """
- **Admissions Trends**: Applications and enrollments fluctuate across terms, with a notable difference between Spring and Fall.
- **Retention & Satisfaction**: Retention and satisfaction trends indicate overall stability but show variations by year.
- **Department Analysis**: Engineering and Business typically see the highest enrollments, while Arts and Science have steadier numbers.
- **Spring vs. Fall**: Comparing across terms reveals key differences in admission rates and student preferences.
"""
st.markdown(insights)
