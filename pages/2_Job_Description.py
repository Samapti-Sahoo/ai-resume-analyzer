import streamlit as st
from utils import clean_text, extract_skills

st.title("📝 Job Description")

job_text = st.text_area("Paste Job Description")
if not job_description.strip():
    st.warning("Please enter a job description.")
    st.stop()


if job_text:
    cleaned_job = clean_text(job_text)
    st.session_state.job_text = cleaned_job

    job_skills = extract_skills(cleaned_job)

    st.subheader("Required Skills Detected")
    st.write(job_skills)
