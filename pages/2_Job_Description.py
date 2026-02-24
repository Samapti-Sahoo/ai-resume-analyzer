import streamlit as st
from animations import load_animations
from utils import clean_text, extract_skills

# Load Cinematic Theme
load_animations()


# Page Title

st.markdown(
'<div class="title">📝 Job Description</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Enter Job Requirements For AI Matching</div>',
unsafe_allow_html=True
)



# Job Description Box

st.markdown('<div class="card">',unsafe_allow_html=True)

job_text = st.text_area(
"Paste Job Description",
height=250
)

st.markdown('</div>',unsafe_allow_html=True)



# Process Job Description

if job_text:

    cleaned_job = clean_text(job_text)

    st.session_state.job_text = cleaned_job

    skills = extract_skills(cleaned_job)


    st.markdown("""

<div class="card">

<h3>Detected Skills</h3>

</div>

""",unsafe_allow_html=True)


    st.write(skills)


    st.success("Job Description Saved ✅")


else:

    st.markdown("""

<div class="card">

Enter Job Description To Continue →

</div>

""",unsafe_allow_html=True)