import streamlit as st
from animations import load_animations

st.set_page_config(
page_title="AI Resume Analyzer",
layout="wide"
)

load_animations()



st.markdown("""

<div class="title">

🚀 AI Resume Analyzer

</div>

""",unsafe_allow_html=True)



st.markdown("""

<div class="subtitle">

Smart Resume Intelligence System

</div>

""",unsafe_allow_html=True)



st.write("")
st.write("")


col1,col2,col3=st.columns(3)



with col1:

    st.markdown("""

<div class="card">

<h2>📄 Upload Resume</h2>

<p>Upload Resume PDF</p>

</div>

""",unsafe_allow_html=True)

    if st.button("Open Upload"):

        st.switch_page("pages/1_Resume_Upload.py")



with col2:

    st.markdown("""

<div class="card">

<h2>🧠 AI Matching</h2>

<p>Compare Resume and Job</p>

</div>

""",unsafe_allow_html=True)


    if st.button("Open Matching"):

        st.switch_page("pages/3_Analysis_Dashboard.py")



with col3:

    st.markdown("""

<div class="card">

<h2>📊 ATS Score</h2>

<p>Check ATS Compatibility</p>

</div>

""",unsafe_allow_html=True)


    if st.button("Open ATS"):

        st.switch_page("pages/4_ATS_Checker.py")



st.sidebar.title("Navigation")

st.sidebar.write("📄 Resume Upload")
st.sidebar.write("🧠 Job Description")
st.sidebar.write("📊 Dashboard")
st.sidebar.write("⭐ ATS Checker")