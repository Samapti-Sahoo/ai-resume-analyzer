import streamlit as st
from animations import load_animations
from utils import extract_text_from_pdf

load_animations()

st.markdown('<div class="title">📄 Upload Resume</div>',unsafe_allow_html=True)

st.markdown('<div class="card">',unsafe_allow_html=True)

file=st.file_uploader("Upload Resume PDF")

st.markdown('</div>',unsafe_allow_html=True)



if file:

    text=extract_text_from_pdf(file)

    st.session_state.resume_text=text

    st.success("Resume Uploaded")