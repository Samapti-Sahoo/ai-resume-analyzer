import streamlit as st
from animations import load_animations
from utils import extract_skills
from scoring import calculate_similarity, calculate_final_score
import matplotlib.pyplot as plt


# Load Theme
load_animations()



# Title

st.markdown(
'<div class="title">📊 AI Analysis Dashboard</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Smart Resume vs Job Matching</div>',
unsafe_allow_html=True
)



# Check Data

if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.markdown("""

<div class="card">

Upload Resume and Job Description First

</div>

""",unsafe_allow_html=True)

    st.stop()



resume = st.session_state.resume_text
job = st.session_state.job_text



# AI Matching

similarity = calculate_similarity(resume, job)

resume_skills = extract_skills(resume)
job_skills = extract_skills(job)


matched = list(set(resume_skills) & set(job_skills))
missing = list(set(job_skills) - set(resume_skills))


skill_ratio = len(matched) / len(job_skills) if job_skills else 0

ats_score = 80 if len(resume_skills) > 5 else 60

final_score = calculate_final_score(
    similarity,
    skill_ratio,
    ats_score
)



# SCORE SECTION

st.markdown("""
<div class="card">
<h2>Resume Score</h2>
</div>
""",unsafe_allow_html=True)



st.progress(int(final_score))


st.metric(
"Final Resume Score",
f"{int(final_score)}%"
)



# MATCHED SKILLS

st.markdown("""
<div class="card">
<h3>Matched Skills</h3>
</div>
""",unsafe_allow_html=True)


if matched:

    for skill in matched:

        st.success(skill)

else:

    st.warning("No matched skills")



# MISSING SKILLS

st.markdown("""
<div class="card">
<h3>Missing Skills</h3>
</div>
""",unsafe_allow_html=True)


if missing:

    for skill in missing:

        st.error(skill)

else:

    st.success("No missing skills")



# PIE CHART

labels = ["Matched","Missing"]

sizes = [len(matched),len(missing)]



if sum(sizes) > 0:

    fig, ax = plt.subplots()

    ax.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%'
    )

    st.pyplot(fig)