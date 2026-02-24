import streamlit as st
from animations import load_animations
from utils import clean_text, extract_skills

load_animations()

st.markdown('<div class="title">📝 Job Description</div>',unsafe_allow_html=True)


job_text = st.text_area(
"Paste Job Description Here",
height=250
)


if job_text:

    cleaned_job = clean_text(job_text)

    st.session_state.job_text = cleaned_job

    skills = extract_skills(cleaned_job)

    st.success("✅ Job Description Saved")

    st.markdown("### 🎯 Required Skills")

    if skills:

        for s in skills:
            st.write("✔",s)

    else:
        st.warning("No skills detected")