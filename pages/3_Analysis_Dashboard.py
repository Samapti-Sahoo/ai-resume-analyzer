import streamlit as st
import matplotlib.pyplot as plt
from scoring import calculate_similarity, calculate_final_score
from utils import extract_skills

st.markdown('<div class="main-title">Analysis Dashboard</div>',unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)


# Check data exists

if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.warning("Upload Resume and Job Description First")

    st.stop()



resume = st.session_state.resume_text
job = st.session_state.job_text


similarity = calculate_similarity(resume,job)

resume_skills = extract_skills(resume)
job_skills = extract_skills(job)


matched=list(set(resume_skills)&set(job_skills))

missing=list(set(job_skills)-set(resume_skills))


skill_ratio=len(matched)/len(job_skills) if job_skills else 0

ats_score=80 if len(resume_skills)>5 else 60

final_score=calculate_final_score(similarity,skill_ratio,ats_score)


st.markdown("<br>",unsafe_allow_html=True)


# Score Circle

st.markdown(f"""
<div class="score">
{final_score}%
</div>
""",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)


col1,col2=st.columns(2)


# Matched Skills Card

with col1:

 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("✅ Matched Skills")

 st.success(matched)

 st.markdown('</div>',unsafe_allow_html=True)



# Missing Skills Card

with col2:

 st.markdown('<div class="glass">',unsafe_allow_html=True)

 st.subheader("❌ Missing Skills")

 st.error(missing)

 st.markdown('</div>',unsafe_allow_html=True)



st.markdown("<br>",unsafe_allow_html=True)


# Skill Match Chart

labels=['Matched','Missing']

sizes=[len(matched),len(missing)]


if sum(sizes)>0:

 fig,ax=plt.subplots(figsize=(5,5))

 colors=["#22d3ee","#6366f1"]

 ax.pie(

 sizes,

 labels=labels,

 autopct='%1.1f%%',

 colors=colors

 )

 st.pyplot(fig)



st.markdown("<br>",unsafe_allow_html=True)


# Skill Progress Bars

st.markdown('<div class="glass">',unsafe_allow_html=True)

st.subheader("📊 Skill Match Meter")

st.progress(int(skill_ratio*100))

st.write("Match Percentage:",int(skill_ratio*100),"%")

st.markdown('</div>',unsafe_allow_html=True)