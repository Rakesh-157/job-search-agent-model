import streamlit as st

# Dummy job data (we will replace with real API later)
jobs = [
    {"title": "Python Developer", "location": "Bangalore", "skills": ["python", "django"], "salary": "5 LPA"},
    {"title": "Frontend Developer", "location": "Mumbai", "skills": ["html", "css", "javascript"], "salary": "4 LPA"},
    {"title": "Data Analyst", "location": "Delhi", "skills": ["python", "sql", "excel"], "salary": "6 LPA"},
]

st.title("Job Search AI Agent")

# User input
skill_input = st.text_input("Enter your skills (comma separated)")
location_input = st.text_input("Preferred location")

if st.button("Search Jobs"):
    user_skills = [s.strip().lower() for s in skill_input.split(",")]

    results = []

    for job in jobs:
        match_count = len(set(user_skills) & set(job["skills"]))

        if location_input.lower() in job["location"].lower() and match_count > 0:
            results.append((job, match_count))

    if results:
        st.subheader("Matching Jobs")
        for job, score in results:
            st.write(f"**{job['title']}**")
            st.write(f"{job['location']}")
            st.write(f"{job['salary']}")
            st.write(f"Match Score: {score}")
            st.write("---")
    else:
        st.warning("No matching jobs found")




import streamlit as st
from PyPDF2 import PdfReader

st.title("AI Job Assistant ")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.success("Resume uploaded successfully!")

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text:")
    st.write(text[:1000]) 

