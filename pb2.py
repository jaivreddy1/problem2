import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data function
@st.cache_data
def load_data(file_path="university_student_dashboard_data.csv"):
    return pd.read_csv(file_path)

# Load dataset
df = load_data()

# Streamlit app title
st.title("📊 University Admissions & Student Satisfaction Dashboard")

# Year filter
st.sidebar.header("🔍 Filters")
selected_year = st.sidebar.selectbox("Select Year", df['Year'].unique())

# Filter data based on selected year
df_filtered = df[df['Year'] == selected_year]

# --- Applications, Admissions, and Enrollments ---
st.subheader("📈 Applications, Admissions, and Enrollments Over Time")
fig, ax = plt.subplots()
ax.plot(df_filtered['Term'], df_filtered['Applications'], label='Applications', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Admitted'], label='Admitted', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Enrolled'], label='Enrolled', marker='o')
ax.set_ylabel("Count")
ax.set_title("Admissions Trends")
ax.legend()
st.pyplot(fig)

# --- Retention and Satisfaction Trends ---
st.subheader("📊 Retention Rate & Student Satisfaction")
fig, ax = plt.subplots()
ax.plot(df_filtered['Term'], df_filtered['Retention Rate (%)'], label='Retention Rate', marker='o')
ax.plot(df_filtered['Term'], df_filtered['Student Satisfaction (%)'], label='Satisfaction', marker='o')
ax.set_ylabel("Percentage")
ax.set_title("Retention & Satisfaction Trends")
ax.legend()
st.pyplot(fig)

# --- Enrollment Breakdown by Department ---
st.subheader("🎓 Enrollment Breakdown by Department")
departments = ['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']
department_counts = df_filtered[departments].sum()
fig, ax = plt.subplots()
ax.bar(departments, department_counts, color=['blue', 'green', 'red', 'purple'])
ax.set_ylabel("Number of Students")
ax.set_title("Department-wise Enrollment")
st.pyplot(fig)

# --- Key Insights ---
st.subheader("📌 Key Insights")
st.markdown("""
- **Admissions Trends**: Applications and enrollments fluctuate across terms, with notable differences between Spring and Fall.
- **Retention & Satisfaction**: Retention and satisfaction trends indicate overall stability but vary by year.
- **Department Analysis**: Engineering and Business have the highest enrollments, while Arts and Science maintain steady numbers.
- **Spring vs. Fall**: Comparing terms reveals key differences in admission rates and student preferences.
""")
