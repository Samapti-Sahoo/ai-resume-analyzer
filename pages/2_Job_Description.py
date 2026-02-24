import streamlit as st
from utils import clean_text,extract_skills
from style import load_css

st.markdown(load_css(),unsafe_allow_html=True)

st.title("📝 Job Description")

job=st.text_area("Paste Job Description")


if job:

    cleaned=clean_text(job)

    st.session_state.job_text=cleaned

    skills=extract_skills(cleaned)

    st.subheader("Detected Skills")

    st.write(skills)