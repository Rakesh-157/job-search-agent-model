import streamlit as st
import pdfplumber
from groq import Groq
from serpapi import GoogleSearch

st.set_page_config(page_title="CareerPilot AI", layout="wide")

st.title("CareerPilot AI")
st.subheader("Smart Job Search & Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Your Resume",
    type=["pdf"]
)

if uploaded_file:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    st.success("Resume Uploaded Successfully!")

    st.subheader("Resume Text")
    st.write(text)

    # ATS Score

    keywords = [
        "python",
        "java",
        "sql",
        "machine learning",
        "data analytics",
        "power bi",
        "excel",
        "pandas",
        "numpy",
        "scikit",
        "mysql",
        "flask",
        "opencv",
        "project",
        "communication",
        "teamwork"
    ]

    score = 0
    found_skills = []

    for skill in keywords:
        if skill.lower() in text.lower():
            score += 10
            found_skills.append(skill)

    if score > 100:
        score = 100

    st.subheader("ATS Score")
    st.metric("Score", f"{score}/100")

    st.subheader("Detected Skills")
    st.write(found_skills)

    # Recommended Jobs

    st.subheader("Recommended Jobs")

    jobs = []

    if "python" in found_skills:
        jobs.append("Python Developer")

    if "sql" in found_skills:
        jobs.append("Data Analyst")

    if "machine learning" in found_skills:
        jobs.append("Machine Learning Engineer")

    if "power bi" in found_skills:
        jobs.append("Business Intelligence Analyst")

    if "flask" in found_skills:
        jobs.append("Backend Developer")

    if len(jobs) > 0:
        for job in jobs:
            st.success(job)
    else:
        st.warning("No matching jobs found")

    # Skill Gap Analysis

    st.subheader("Skill Gap Analysis")

    required_skills = [
        "python",
        "sql",
        "machine learning",
        "power bi",
        "communication",
        "teamwork"
    ]

    missing_skills = []

    for skill in required_skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    if missing_skills:
        st.warning("Missing Skills")
        st.write(missing_skills)
    else:
        st.success("No major skill gaps found!")

    # Resume Improvement Tips

    st.subheader("Resume Improvement Suggestions")

    st.info("""
    • Add more technical skills

    • Include internship experience

    • Add measurable project outcomes

    • Mention certifications clearly

    • Improve ATS keywords

    • Add LinkedIn and GitHub profiles
    """)

    # Salary Estimation

    st.subheader("Estimated Salary Range")

    if "machine learning" in found_skills:
        st.success("Machine Learning Engineer : ₹6 - ₹12 LPA")

    if "python" in found_skills:
        st.success("Python Developer : ₹4 - ₹8 LPA")

    if "sql" in found_skills:
        st.success("Data Analyst : ₹4 - ₹10 LPA")

client = Groq(
    api_key="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"
)
SERP_API_KEY = "052622dbee00db39c9b486d861455d5a677459068506a030271b5988593bcbee"

st.subheader("🤖 AI Resume Analysis")

if uploaded_file:

    if st.button("Analyze Resume with AI"):

        prompt = f"""
        Analyze this resume.

        Resume:
        {text}

        Give:
        1. ATS Score out of 100
        2. Strengths
        3. Weaknesses
        4. Missing Skills
        5. Suggested Job Roles
        6. Resume Improvement Tips
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        result = response.choices[0].message.content

        st.write(result)


st.subheader(" AI Job Search")

job_role = st.text_input(
    "Enter Job Role",
    "Python Developer"
)

job_location = st.text_input(
    "Enter Location",
    "Bangalore"
)

if st.button("Search Jobs"):

    params = {
        "engine": "google_jobs",
        "q": f"{job_role} jobs in {job_location}",
        "hl": "en",
        "api_key": SERP_API_KEY
    }

    search = GoogleSearch(params)

    results = search.get_dict()

    jobs = results.get("jobs_results", [])

    if jobs:

        for job in jobs[:5]:

            st.success(
                job.get("title", "N/A")
            )

            st.write(
                " Company:",
                job.get("company_name", "N/A")
            )

            st.write(
                " Location:",
                job.get("location", "N/A")
            )

            st.write(
                " Posted:",
                job.get("detected_extensions", {})
                .get("posted_at", "N/A")
            )

            st.write("---")

    else:
        st.warning("No jobs found")
