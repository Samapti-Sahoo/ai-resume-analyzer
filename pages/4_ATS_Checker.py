import streamlit as st
from scoring import calculate_similarity
from utils import extract_skills


# ---------- DESIGN ----------

st.markdown("""

<style>

.box{

background:rgba(255,255,255,0.05);

padding:25px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.1);

margin-bottom:20px;

}

.good{

color:#22c55e;
font-weight:bold;

}

.bad{

color:#ef4444;
font-weight:bold;

}

</style>

""",unsafe_allow_html=True)



# ---------- TITLE ----------

st.markdown("# 🎯 ATS Compatibility Checker")

st.write("Check Resume ATS Compatibility")

st.write("")


# ---------- CHECK ----------

if "resume_text" not in st.session_state or "job_text" not in st.session_state:

    st.warning("Upload Resume and Job Description First")

    st.stop()


resume = st.session_state.resume_text
job = st.session_state.job_text


# ---------- SCORE ----------

similarity = calculate_similarity(resume,job)

ats_score=int(similarity*100)


st.subheader("ATS Score")

st.progress(ats_score)

st.metric("Compatibility",f"{ats_score}%")

st.write("")


# ---------- ANALYSIS ----------

resume_skills = extract_skills(resume)
job_skills = extract_skills(job)


matched=list(set(resume_skills)&set(job_skills))

missing=list(set(job_skills)-set(resume_skills))


# ---------- GOOD POINTS ----------

st.markdown('<div class="box">',unsafe_allow_html=True)

st.subheader("Good Points")

if len(matched)>0:

    for s in matched:

        st.markdown(f"<span class='good'>✔ {s}</span>",unsafe_allow_html=True)

else:

    st.write("No matched skills found")


st.markdown('</div>',unsafe_allow_html=True)



# ---------- IMPROVEMENTS ----------

st.markdown('<div class="box">',unsafe_allow_html=True)

st.subheader("Improve Your Resume")

if len(missing)>0:

    for s in missing:

        st.markdown(f"<span class='bad'>✘ Add skill: {s}</span>",unsafe_allow_html=True)

else:

    st.write("Resume looks good")


st.markdown('</div>',unsafe_allow_html=True)