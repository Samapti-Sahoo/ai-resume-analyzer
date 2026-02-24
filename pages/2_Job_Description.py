import streamlit as st
from animations import load_animations
from utils import clean_text,extract_skills

load_animations()


st.markdown("""

<div class="title">

📋 Job Description

</div>

""",unsafe_allow_html=True)



job=st.text_area("Paste Job Description")



if job:

    clean=clean_text(job)

    st.session_state.job_text=clean

    skills=extract_skills(clean)

    st.write(skills)