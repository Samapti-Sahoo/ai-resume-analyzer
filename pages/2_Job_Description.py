import streamlit as st
from animations import load_animations

load_animations()

st.markdown('<div class="title">🧠 Job Description</div>',unsafe_allow_html=True)


job=st.text_area("Paste Job Description")


if job:

    st.session_state.job_text=job

    st.success("Job Description Saved")