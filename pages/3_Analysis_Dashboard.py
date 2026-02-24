import streamlit as st
import matplotlib.pyplot as plt
from scoring import calculate_similarity, calculate_final_score
from utils import extract_skills


# ---------- DESIGN ----------

st.markdown("""

<style>

/* Score Cards */

.card{

background:rgba(255,255,255,0.05);

padding:25px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.1);

text-align:center;

margin-bottom:20px;

}

/* Skill Tag */

.skill{

background:rgba(59,130,246,0.3);

padding:8px 16px;

border-radius:20px;

margin:5px;

display:inline-block;

font-weight:bold;

}

/* Missing */

.missing{

background:rgba(255,80,80,0.3);

padding:8px 16px;

border-radius:20px;

margin:5px;

display:inline-block;

font-weight:bold;

}

</style>

""",unsafe_allow_html=True)


# ---------- TITLE ----------

st.markdown("# 📊 AI Analysis Dashboard")

st.write("Smart Resume Analysis Report")

st.write("")


# ---------- CHECK DATA ----------

if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.warning("Upload Resume and Job Description First")

    st.stop()


resume = st.session_state.resume_text
job = st.session_state.job_text


# ---------- AI SCORES ----------

similarity = calculate_similarity(resume,job)

resume_skills = extract_skills(resume)
job_skills = extract_skills(job)

matched = list(set(resume_skills)&set(job_skills))
missing = list(set(job_skills)-set(resume_skills))


skill_ratio = len(matched)/len(job_skills) if job_skills else 0

ats_score = 80 if len(resume_skills)>5 else 60

final_score = calculate_final_score(similarity,skill_ratio,ats_score)


# ---------- SCORE CARDS ----------

c1,c2,c3 = st.columns(3)

with c1:

    st.markdown(f"""
    <div class="card">

    <h2>{int(similarity*100)}%</h2>

    Similarity Score

    </div>

    """,unsafe_allow_html=True)


with c2:

    st.markdown(f"""
    <div class="card">

    <h2>{ats_score}%</h2>

    ATS Score

    </div>

    """,unsafe_allow_html=True)



with c3:

    st.markdown(f"""
    <div class="card">

    <h2>{int(final_score)}%</h2>

    Final Score

    </div>

    """,unsafe_allow_html=True)



st.write("")



# ---------- PROGRESS BAR ----------

st.subheader("Overall Match Score")

st.progress(int(final_score))


st.write("")


# ---------- MATCHED SKILLS ----------

st.subheader("Matched Skills")

for s in matched:

    st.markdown(
    f'<span class="skill">{s}</span>',
    unsafe_allow_html=True
    )


st.write("")


# ---------- MISSING SKILLS ----------

st.subheader("Missing Skills")

for s in missing:

    st.markdown(
    f'<span class="missing">{s}</span>',
    unsafe_allow_html=True
    )


st.write("")


# ---------- PIE CHART ----------

labels=["Matched","Missing"]

sizes=[len(matched),len(missing)]


if sum(sizes)>0:

    fig,ax=plt.subplots()

    ax.pie(

    sizes,

    labels=labels,

    autopct='%1.1f%%'

    )

    st.pyplot(fig)