import streamlit as st
from animations import load_animations

st.set_page_config(layout="wide")

load_animations()

st.markdown('<div class="title">🚀 AI Resume Analyzer</div>',unsafe_allow_html=True)

st.markdown('<div class="subtitle">Smart Resume Intelligence System</div>',unsafe_allow_html=True)

st.write("")
st.write("")


col1,col2,col3=st.columns(3)



# ---------- CARD 1 ----------

with col1:

    if st.button("📄 Upload Resume",use_container_width=True):

        st.switch_page("pages/1_Resume_Upload.py")

    st.markdown("""

<div class="card">

<h2>📄 Upload Resume</h2>

<p>Upload Resume PDF</p>

</div>

""",unsafe_allow_html=True)



# ---------- CARD 2 ----------

with col2:

    if st.button("🧠 AI Matching",use_container_width=True):

        st.switch_page("pages/3_Analysis_Dashboard.py")

    st.markdown("""

<div class="card">

<h2>🧠 AI Matching</h2>

<p>Analyze Resume Skills</p>

</div>

""",unsafe_allow_html=True)



# ---------- CARD 3 ----------

with col3:

    if st.button("📊 ATS Score",use_container_width=True):

        st.switch_page("pages/4_ATS_Checker.py")

    st.markdown("""

<div class="card">

<h2>📊 ATS Score</h2>

<p>Check ATS Compatibility</p>

</div>

""",unsafe_allow_html=True)