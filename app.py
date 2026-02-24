import streamlit as st
from animations import load_animations

load_animations()

st.set_page_config(
page_title="AI Resume Analyzer",
layout="wide"
)



# Rocket

st.markdown('<div class="rocket">🚀</div>',unsafe_allow_html=True)



# Title

st.markdown("""

<div class="title">

AI Resume Analyzer

</div>

""",unsafe_allow_html=True)



st.markdown("""

<div class="subtitle">

Cinematic AI Resume Intelligence

</div>

""",unsafe_allow_html=True)



col1,col2,col3=st.columns(3)



# Upload Card

with col1:

    if st.button("📄 Upload Resume"):

        st.switch_page("pages/1_Resume_Upload.py")



    st.markdown("""

<div class="card">

<h1>📄</h1>

<h2>Upload Resume</h2>

<p>Upload Resume PDF</p>

</div>

""",unsafe_allow_html=True)



# Matching Card

with col2:

    if st.button("🧠 AI Matching"):

        st.switch_page("pages/3_Analysis_Dashboard.py")



    st.markdown("""

<div class="card">

<h1>🧠</h1>

<h2>AI Matching</h2>

<p>Analyze Resume Skills</p>

</div>

""",unsafe_allow_html=True)



# ATS Card

with col3:

    if st.button("📊 ATS Score"):

        st.switch_page("pages/4_ATS_Checker.py")



    st.markdown("""

<div class="card">

<h1>📊</h1>

<h2>ATS Score</h2>

<p>Check ATS Compatibility</p>

</div>

""",unsafe_allow_html=True)



st.write("")

st.success("Click Cards Or Use Sidebar")