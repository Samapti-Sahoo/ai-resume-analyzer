import streamlit as st
from animations import load_animations
from utils import extract_skills

load_animations()

st.markdown('<div class="title">📈 ATS Checker</div>',unsafe_allow_html=True)



if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()



resume=st.session_state.resume_text

skills=extract_skills(resume)



st.markdown("### ATS Result")


score=len(skills)*5

if score>100:
    score=100



st.metric("ATS Score",str(score)+"%")


st.progress(score)



st.markdown("### Skills Detected")

for s in skills:

    st.write("✔",s)



if score>80:

    st.success("Excellent ATS Resume")


elif score>60:

    st.info("Good Resume")


else:

    st.error("Needs Improvement")