import streamlit as st
from animations import load_animations

st.set_page_config(
page_title="AI Resume Analyzer",
layout="wide"
)

load_animations()



# NAVBAR

st.markdown("""

<div class="navbar">

<div class="logo">

🚀 ResumeAI

</div>

<div class="nav-links">

<a href="?page=home">Home</a>

<a href="?page=upload">Upload</a>

<a href="?page=analysis">Analysis</a>

<a href="?page=ats">ATS</a>

</div>

</div>

""",unsafe_allow_html=True)



# HERO

st.markdown("""

<div class="hero">

<h1>🚀 AI Resume Analyzer</h1>

<p>Cinematic AI Resume Intelligence</p>

</div>

""",unsafe_allow_html=True)



# CARDS

st.markdown("""

<div class="grid">

<div class="card">

<h2>📄 Upload Resume</h2>

<p>Upload Resume PDF</p>

<a class="btn" href="?page=upload">

Open Upload

</a>

</div>



<div class="card">

<h2>🧠 AI Matching</h2>

<p>Analyze Resume Skills</p>

<a class="btn" href="?page=analysis">

Open Matching

</a>

</div>



<div class="card">

<h2>📊 ATS Score</h2>

<p>Check ATS Compatibility</p>

<a class="btn" href="?page=ats">

Open ATS

</a>

</div>


</div>

""",unsafe_allow_html=True)