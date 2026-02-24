import streamlit as st
from scoring import calculate_similarity,calculate_final_score
from utils import extract_skills
from style import load_css

st.markdown(load_css(),unsafe_allow_html=True)

st.title("📊 Analysis Dashboard")


if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.warning("Upload resume and job description")

    st.stop()


resume=st.session_state.resume_text
job=st.session_state.job_text


similarity=calculate_similarity(resume,job)

resume_skills=extract_skills(resume)
job_skills=extract_skills(job)

matched=list(set(resume_skills)&set(job_skills))
missing=list(set(job_skills)-set(resume_skills))


c1,c2,c3=st.columns(3)


c1.metric("Similarity",str(int(similarity*100))+"%")

c2.metric("Matched Skills",len(matched))

c3.metric("Missing Skills",len(missing))


st.subheader("Matched Skills")

st.write(matched)


st.subheader("Missing Skills")

st.write(missing)