import streamlit as st
from animations import load_animations
from scoring import calculate_similarity, calculate_final_score
from utils import extract_skills


load_animations()


st.markdown("""

<div class="hero">

<h1>📊 AI Analysis</h1>

<p>Smart Resume Intelligence</p>

</div>

""",unsafe_allow_html=True)


if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()


if "job_text" not in st.session_state:

    st.warning("Add Job Description First")

    st.stop()



resume = st.session_state.resume_text

job = st.session_state.job_text


similarity = calculate_similarity(resume,job)


resume_skills = extract_skills(resume)

job_skills = extract_skills(job)


matched = list(set(resume_skills) & set(job_skills))

missing = list(set(job_skills) - set(resume_skills))


skill_ratio = len(matched)/len(job_skills) if job_skills else 0

ats_score = 80 if len(resume_skills)>5 else 60


final_score = calculate_final_score(
similarity,
skill_ratio,
ats_score
)


st.markdown("## Final Resume Score")

st.metric("Score",f"{int(final_score)}%")


st.progress(int(final_score))


st.write("")


col1,col2 = st.columns(2)


with col1:

    st.markdown("### Matched Skills")

    st.write(matched)



with col2:

    st.markdown("### Missing Skills")

    st.write(missing)