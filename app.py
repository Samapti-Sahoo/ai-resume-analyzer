import streamlit as st
from animations import load_animations
import time

st.set_page_config(layout="wide")

load_animations()

st.markdown('<div class="title">🚀 AI Resume Analyzer</div>',unsafe_allow_html=True)

st.markdown('<div class="subtitle">Cinematic AI Resume Intelligence</div>',unsafe_allow_html=True)


col1,col2,col3=st.columns(3)


# CARD 1

with col1:

    click1=st.button("upload",use_container_width=True)

    st.markdown("""

<div class="card">

<h2>📄 Upload Resume</h2>

<p>Upload Resume PDF</p>

</div>

""",unsafe_allow_html=True)

    if click1:

        st.spinner("Opening Upload...")

        time.sleep(0.4)

        st.switch_page("pages/1_Resume_Upload.py")



# CARD 2

with col2:

    click2=st.button("matching",use_container_width=True)

    st.markdown("""

<div class="card">

<h2>🧠 AI Matching</h2>

<p>Analyze Resume Skills</p>

</div>

""",unsafe_allow_html=True)

    if click2:

        st.spinner("Opening Matching...")

        time.sleep(0.4)

        st.switch_page("pages/3_Analysis_Dashboard.py")



# CARD 3

with col3:

    click3=st.button("ats",use_container_width=True)

    st.markdown("""

<div class="card">

<h2>📊 ATS Score</h2>

<p>Check ATS Compatibility</p>

</div>

""",unsafe_allow_html=True)

    if click3:

        st.spinner("Opening ATS...")

        time.sleep(0.4)

        st.switch_page("pages/4_ATS_Checker.py")