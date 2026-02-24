import streamlit as st
from animations import load_animations

st.set_page_config(
page_title="AI Resume Analyzer",
layout="wide"
)

load_animations()

st.markdown("<h1 style='text-align:center'>🚀 AI Resume Analyzer</h1>",unsafe_allow_html=True)

st.markdown(
"<h3 style='text-align:center;color:gray'>Futuristic Resume Intelligence</h3>",
unsafe_allow_html=True
)



col1,col2,col3 = st.columns(3)


with col1:

    if st.button("📄 Upload Resume"):

        st.switch_page("pages/1_Resume_Upload.py")


    st.markdown("""

<div class="card">

<h2>Upload Resume</h2>

<p>Smart Resume Parser</p>

</div>

""",unsafe_allow_html=True)



with col2:

    if st.button("🧠 AI Matching"):

        st.switch_page("pages/3_Analysis_Dashboard.py")

    st.markdown("""

<div class="card">

<h2>AI Matching</h2>

<p>Deep Skill Detection</p>

</div>

""",unsafe_allow_html=True)




with col3:

    if st.button("📊 ATS Score"):

        st.switch_page("pages/4_ATS_Checker.py")


    st.markdown("""

<div class="card">

<h2>ATS Score</h2>

<p>Resume Strength</p>

</div>

""",unsafe_allow_html=True)
    
st.sidebar.markdown("""

### Navigation

📄 Resume Upload

🧠 Job Description

📊 Dashboard

⭐ ATS Checker

""") 