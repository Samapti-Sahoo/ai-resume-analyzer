import streamlit as st
from animations import load_animations
from utils import extract_skills

load_animations()


st.markdown("""

<div class="title">

📊 ATS Checker

</div>

""",unsafe_allow_html=True)



if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()



skills=extract_skills(st.session_state.resume_text)



score=len(skills)*5



st.progress(score)

st.metric("ATS Score",score)