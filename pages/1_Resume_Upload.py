import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills

st.markdown("""
<div class="main-title">
Resume Analyzer
</div>
""",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)


# Upload Card

st.markdown('<div class="glass">',unsafe_allow_html=True)

st.subheader("📁 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload PDF Resume",
    type=["pdf"]
)

st.markdown('</div>',unsafe_allow_html=True)


if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    cleaned = clean_text(text)

    st.session_state.resume_text = cleaned

    skills = extract_skills(cleaned)

    st.session_state.resume_skills = skills


    st.markdown("<br>",unsafe_allow_html=True)


    # Skills Card

    st.markdown('<div class="glass">',unsafe_allow_html=True)

    st.subheader("🎯 Skills Detected")

    st.success(skills)

    st.markdown('</div>',unsafe_allow_html=True)