import streamlit as st
from animations import load_animations
from utils import extract_skills
from scoring import calculate_similarity


load_animations()


st.markdown("""

<div class='hero'>

<h1>📊 AI Analysis</h1>

<p>Smart Resume Intelligence</p>

</div>

""",unsafe_allow_html=True)



if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()



resume = st.session_state.resume_text

job = st.session_state.get("job_text","")


score = calculate_similarity(resume,job)



st.markdown("<div class='card'>",unsafe_allow_html=True)

st.metric("Resume Match Score",str(score)+"%")

st.progress(score)

st.markdown("</div>",unsafe_allow_html=True)