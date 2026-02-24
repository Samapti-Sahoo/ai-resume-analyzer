import streamlit as st
from animations import load_animations
from utils import extract_skills
from scoring import calculate_similarity
import math

# Load Cinematic Theme
load_animations()


# Title

st.markdown(
'<div class="title">🎯 ATS Checker</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Professional Resume ATS Analysis</div>',
unsafe_allow_html=True
)



# Check Resume

if "resume_text" not in st.session_state:

    st.markdown("""

<div class="card">
Upload Resume First
</div>

""",unsafe_allow_html=True)

    st.stop()


resume = st.session_state.resume_text


skills = extract_skills(resume)



# ATS Score Logic

ats_score = min(len(skills)*8 ,100)



# Score Card

st.markdown("""

<div class="card">

<h2>ATS Score</h2>

</div>

""",unsafe_allow_html=True)



# Animated Bar

st.progress(ats_score)


st.metric(

"Resume ATS Score",

f"{ats_score}%"

)



# 3D Gauge Meter

st.markdown("""

<div class="card">

<h3>ATS Meter</h3>

</div>

""",unsafe_allow_html=True)



# Gauge Simulation

meter_html = f"""

<div style="
width:300px;
height:150px;
margin:auto;
background:linear-gradient(90deg,#00ffe7,#0066ff);
border-radius:300px 300px 0 0;
box-shadow:0 20px 60px rgba(0,255,200,0.4);
position:relative;
">

<div style="
position:absolute;
bottom:0;
left:{ats_score*3}px;
width:6px;
height:140px;
background:white;
box-shadow:0 0 20px white;
transform-origin:bottom;
">

</div>

</div>

<h2 style="text-align:center">
{ats_score}%
</h2>

"""

st.markdown(meter_html,unsafe_allow_html=True)



# Skills Section

st.markdown("""

<div class="card">

<h3>Detected Skills</h3>

</div>

""",unsafe_allow_html=True)



for s in skills:

    st.success(s)



if not skills:

    st.warning("No skills detected")