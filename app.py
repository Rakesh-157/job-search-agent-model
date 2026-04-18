import streamlit as st
from PyPDF2 import PdfReader

# ---------------- TITLE ----------------
st.title("AI Career Assistant ")

# ---------------- JOB DATA ----------------
jobs = [
    {
        "title": "Python Developer",
        "location": "Bangalore",
        "skills": ["python", "django"],
        "salary": "5 LPA",
        "company": "Infosys",
        "desc": "IT services company"
    },
    {
        "title": "Frontend Developer",
        "location": "Mumbai",
        "skills": ["html", "css", "javascript"],
        "salary": "4 LPA",
        "company": "TCS",
        "desc": "Software company"
    },
    {
        "title": "Data Analyst",
        "location": "Delhi",
        "skills": ["python", "sql", "excel"],
        "salary": "6 LPA",
        "company": "Wipro",
        "desc": "Analytics services"
    }
]

# ---------------- TABS ----------------
tab1, tab2 = st.tabs([" Resume Analyzer", " Job Search"])

# ---------------- RESUME SECTION ----------------
resume_text = ""

with tab1:
    st.header("Upload Resume")

    uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            if page.extract_text():
                resume_text += page.extract_text()

        st.success("Resume uploaded successfully!")
        st.write(resume_text[:500])

# ---------------- JOB SEARCH ----------------
with tab2:
    st.header("Find Jobs")

    skill_input = st.text_input("Enter skills (comma separated)")
    location_input = st.text_input("Preferred location")

    if st.button("Search Jobs"):

        # Decide skill source
        if resume_text.strip() != "":
            user_skills = resume_text.lower().split()
        else:
            user_skills = [s.strip().lower() for s in skill_input.split(",") if s.strip()]

        results = []

        for job in jobs:
            # Skill matching
            match_count = len(set(user_skills) & set(job["skills"]))

            # Smart score
            score = match_count * 2

            if location_input.strip() != "" and location_input.lower() in job["location"].lower():
                score += 1

            # Add only relevant jobs
            if score > 0:
                results.append((job, score))

        # ---------------- DISPLAY RESULTS ----------------
        if results:
            st.success("Based on your profile, here are the best jobs 👇")

            for job, score in results:
                st.write(f"### {job['title']}")
                st.write(f" Location: {job['location']}")
                st.write(f" Salary: {job['salary']}")
                st.write(f" Company: {job['company']}")
                st.write(f" Description: {job['desc']}")
                st.write(f" Match Score: {score}")
                st.write("---")
        else:
            st.warning("No matching jobs found")


# Resume scoring
st.subheader("📊 Resume Score")

score = 0

total_skills = len(skill_keywords)
skill_keywords = [
    "python", "java", "c", "c++", "javascript",
    "html", "css", "react", "node", "django",
    "flask", "sql", "mongodb", "machine learning",
    "data science", "ai", "deep learning",
    "pandas", "numpy", "tensorflow", "git"
]
# define skills first
skill_keywords = ["python", "java", "html", "css"]

# then use it
total_skills = len(skill_keywords)

# Skill score (60 marks)
total_skills = len(skill_keywords)
matched_skills = len(found_skills)

skill_score = (matched_skills / total_skills) * 60
score += skill_score

# Resume length score (20 marks)
word_count = len(resume_text.split())

if word_count > 300:
    score += 20
elif word_count > 200:
    score += 15
elif word_count > 100:
    score += 10
else:
    score += 5

# Projects check (10 marks)
if "project" in resume_text.lower():
    score += 10

# Education check (10 marks)
if "bachelor" in resume_text.lower() or "b.tech" in resume_text.lower():
    score += 10

# Display score
st.write(f"🎯 Resume Score: {int(score)} / 100")

# Suggestions
st.subheader("💡 Suggestions to Improve")

if matched_skills < 5:
    st.write("✔ Add more technical skills")

if word_count < 200:
    st.write("✔ Increase resume content")

if "project" not in resume_text.lower():
    st.write("✔ Add project section")

if "bachelor" not in resume_text.lower():
    st.write("✔ Add education details")
