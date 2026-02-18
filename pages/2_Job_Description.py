import streamlit as st
from utils import clean_text, extract_skills

st.title("📝 Job Description")

job_text = st.text_area("Paste Job Description")

if not job_text.strip():
    st.warning("Please enter a job description.")
    st.stop()

# Clean job description
cleaned_job = clean_text(job_text)

# Save cleaned job text to session state
st.session_state.job_text = cleaned_job

# Extract required skills
job_skills = extract_skills(cleaned_job)

st.subheader("Required Skills Detected")
st.write(job_skills)
