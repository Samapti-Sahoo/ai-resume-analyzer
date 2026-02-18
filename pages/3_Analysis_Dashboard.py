import streamlit as st

import matplotlib.pyplot as plt
from scoring import calculate_similarity, calculate_final_score
from utils import extract_skills

st.title("📊 Analysis Dashboard")
if "resume_text" not in st.session_state or "job_text" not in st.session_state:
    st.warning("Please upload resume and job description first.")
    st.stop()


if "resume_text" in st.session_state and "job_text" in st.session_state:

    resume = st.session_state.resume_text
    job = st.session_state.job_text

    similarity = calculate_similarity(resume, job)

    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job)

    matched = list(set(resume_skills) & set(job_skills))
    missing = list(set(job_skills) - set(resume_skills))

    skill_ratio = len(matched) / len(job_skills) if job_skills else 0

    ats_score = 80 if len(resume_skills) > 5 else 60

    final_score = calculate_final_score(similarity, skill_ratio, ats_score)

    st.metric("Final Resume Score", f"{final_score}%")
    st.progress(int(final_score))

    st.subheader("Matched Skills")
    st.write(matched)

    st.subheader("Missing Skills")
    st.write(missing)

    labels = ['Matched', 'Missing']
    sizes = [len(matched), len(missing)]

if sum(sizes) > 0:
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)
else:
    st.warning("Not enough skill data to generate chart.")


else:
    st.warning("Please upload resume and job description first.")
