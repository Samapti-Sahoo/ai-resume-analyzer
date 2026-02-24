import streamlit as st
from scoring import calculate_similarity,calculate_final_score
from utils import extract_skills
from style import load_css

st.markdown(load_css(),unsafe_allow_html=True)

st.title("📊 ATS Score")


if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()


resume=st.session_state.resume_text


skills=extract_skills(resume)

score=70+len(skills)


st.metric("ATS Score",str(score)+"%")

st.progress(score)