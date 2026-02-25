import streamlit as st
from animations import load_animations


# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)


# -------------------------
# LOAD CINEMATIC DESIGN
# -------------------------

load_animations()



# -------------------------
# HERO SECTION
# -------------------------

st.markdown("""

<div class='hero'>

<h1>🚀 AI Resume Analyzer</h1>

<p>Cinematic AI Resume Intelligence</p>

</div>

""", unsafe_allow_html=True)



st.write("")
st.write("")
st.write("")


# -------------------------
# CLICKABLE MOVIE CARDS
# -------------------------

col1, col2, col3 = st.columns(3)


# Upload Resume Card
with col1:

    st.markdown("""
    <div class="card">
        <h2>📄 Upload Resume</h2>
        <p>Upload Resume PDF</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Upload Page"):
        st.switch_page("pages/1_Resume_Upload.py")



# AI Matching Card
with col2:

    st.markdown("""
    <div class="card">
        <h2>🧠 AI Matching</h2>
        <p>Analyze Resume Skills</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open Matching Page"):
        st.switch_page("pages/3_Analysis_Dashboard.py")



# ATS Card
with col3:

    st.markdown("""
    <div class="card">
        <h2>📊 ATS Score</h2>
        <p>Check ATS Compatibility</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Open ATS Page"):
        st.switch_page("pages/4_ATS_Checker.py")



st.write("")
st.write("")
st.write("")


# -------------------------
# FOOTER INFO
# -------------------------

st.markdown("""

<center>

### Navigate using Sidebar or Cards

</center>

""", unsafe_allow_html=True)