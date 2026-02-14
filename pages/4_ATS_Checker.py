import streamlit as st

st.title("🤖 ATS Compatibility Checker")

if "resume_text" in st.session_state:

    resume = st.session_state.resume_text

    section_score = 100 if "education" in resume and "experience" in resume else 70
    keyword_density = min(len(resume.split()) / 500, 1) * 100

    ats_score = (section_score + keyword_density) / 2

    st.metric("ATS Score", f"{round(ats_score,2)}%")

    if ats_score < 70:
        st.warning("Improve keyword density and add proper sections.")
    else:
        st.success("Your resume is ATS friendly!")

else:
    st.warning("Upload resume first.")
