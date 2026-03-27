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
    st.write(text[:1000])  # show first 1000 characters
