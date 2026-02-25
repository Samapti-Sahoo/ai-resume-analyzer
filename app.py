import streamlit as st
from animations import load_animations

load_animations()

st.markdown("""

<div class="hero">

<h1>🚀 AI Resume Analyzer</h1>

<p>
Professional Resume Intelligence Platform
</p>

</div>

""",unsafe_allow_html=True)


st.write("")

st.write("")

st.markdown("## How It Works")



col1,col2,col3=st.columns(3)



with col1:

    if st.button("📄 Upload Resume"):

        st.switch_page("pages/1_Resume_Upload.py")



with col2:

    if st.button("📝 Add Job Description"):

        st.switch_page("pages/2_Job_Description.py")



with col3:

    if st.button("📊 View Analysis"):

        st.switch_page("pages/3_Analysis_Dashboard.py")



st.write("")

st.write("")



st.markdown("""

### Why Use This AI Tool?


✔ Smart Resume Matching  

✔ ATS Optimization  

✔ Skill Detection  

✔ AI Based Score


""")