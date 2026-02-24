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


<<<<<<< HEAD
if job_text:

 cleaned=clean_text(job_text)

 st.session_state.job_text=cleaned


 skills=extract_skills(cleaned)


 st.markdown("<br>",unsafe_allow_html=True)


 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("🎯 Required Skills Detected")

 st.success(skills)

 st.markdown('</div>',unsafe_allow_html=True)
=======
if not job_text.strip():
    st.warning("Please enter a job description.")
    st.stop()

# Clean job description
cleaned_job = clean_text(job_text)

# Save cleaned job text to session state
st.session_state.job_text = cleaned_job

# Extract required skills
job_skills = extract_skills(cleaned_job)

st.subheader("Required Skills Detected")
st.write(job_skills)
>>>>>>> 4d8c990fd13454e69eb315505811905e6e37dccd
