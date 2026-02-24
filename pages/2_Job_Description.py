import streamlit as st
from utils import clean_text, extract_skills

st.markdown('<div class="main-title">Job Description</div>',unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)


# Glass Card

st.markdown('<div class="glass">',unsafe_allow_html=True)

st.subheader("📄 Paste Job Description")

job_text=st.text_area(

"",
height=250,

placeholder="Paste job description here..."

)

st.markdown('</div>',unsafe_allow_html=True)


if job_text:

 cleaned=clean_text(job_text)

 st.session_state.job_text=cleaned


 skills=extract_skills(cleaned)


 st.markdown("<br>",unsafe_allow_html=True)


 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("🎯 Required Skills Detected")

 st.success(skills)

 st.markdown('</div>',unsafe_allow_html=True)