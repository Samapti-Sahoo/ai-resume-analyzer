import streamlit as st
from animations import load_animations

st.set_page_config(
page_title="AI Resume Analyzer",
layout="wide"
)

load_animations()


st.markdown('<div class="rocket">🚀</div>',unsafe_allow_html=True)


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



# Upload

with col1:

    st.markdown("""

<div class="card">

<h1>📄</h1>

<h2>Upload Resume</h2>

<p>Upload Resume PDF</p>

</div>

""",unsafe_allow_html=True)

    if st.button("Upload Page"):

        st.switch_page("pages/1_Resume_Upload.py")



# Matching

with col2:

    st.markdown("""

<div class="card">

<h1>🧠</h1>

<h2>AI Matching</h2>

<p>Analyze Resume Skills</p>

</div>

""",unsafe_allow_html=True)

    if st.button("Matching Page"):

        st.switch_page("pages/3_Analysis_Dashboard.py")



# ATS

with col3:

    st.markdown("""

<div class="card">

<h1>📊</h1>

<h2>ATS Score</h2>

<p>Check ATS Compatibility</p>

</div>

""",unsafe_allow_html=True)

    if st.button("ATS Page"):

        st.switch_page("pages/4_ATS_Checker.py")



st.write("")

st.success("Use Sidebar Or Click Boxes")