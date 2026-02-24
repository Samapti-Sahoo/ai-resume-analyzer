import streamlit as st
from scoring import calculate_similarity
from utils import extract_skills

st.markdown('<div class="main-title">ATS Checker</div>',unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.markdown('<div class="glass">',unsafe_allow_html=True)

    st.warning("Upload Resume and Job Description First")

    st.markdown('</div>',unsafe_allow_html=True)

    st.stop()



resume=st.session_state.resume_text
job=st.session_state.job_text


similarity=calculate_similarity(resume,job)


resume_skills=extract_skills(resume)
job_skills=extract_skills(job)


matched=list(set(resume_skills)&set(job_skills))

missing=list(set(job_skills)-set(resume_skills))


ats_score=int(similarity*100)


st.markdown('<div class="glass">',unsafe_allow_html=True)

st.subheader("ATS Score")

st.metric("Match Percentage",f"{ats_score}%")

st.progress(ats_score)

st.markdown('</div>',unsafe_allow_html=True)


st.markdown("<br>",unsafe_allow_html=True)


col1,col2=st.columns(2)

with col1:

 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("Matched Skills")

 st.success(matched)

 st.markdown('</div>',unsafe_allow_html=True)


with col2:

 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("Missing Skills")

 st.error(missing)

 st.markdown('</div>',unsafe_allow_html=True)