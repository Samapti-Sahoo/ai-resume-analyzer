import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills

st.title("📄 Resume Upload")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    cleaned_text = clean_text(text)

    st.session_state.resume_text = cleaned_text
    skills_found = extract_skills(cleaned_text)

    st.subheader("Detected Skills")
    st.write(skills_found)

    st.subheader("Word Count")
    st.write(len(cleaned_text.split()))
