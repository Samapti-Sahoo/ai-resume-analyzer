import streamlit as st
from utils import clean_text, extract_skills


# ---------- DESIGN ----------

st.markdown("""

<style>

/* Text Box */

textarea {

background:rgba(255,255,255,0.05) !important;

border-radius:15px !important;

border:1px solid rgba(255,255,255,0.1) !important;

color:white !important;

font-size:16px !important;

}


/* Skill Tag */

.skill-tag{

background:rgba(59,130,246,0.3);

padding:10px 18px;

border-radius:20px;

margin:5px;

display:inline-block;

font-weight:bold;

}


/* Box */

.big-box{

background:rgba(255,255,255,0.05);

padding:30px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.1);

}

</style>

""",unsafe_allow_html=True)



# ---------- TITLE ----------

st.markdown("# 🧾 Job Description")

st.write("Paste Job Description for AI Analysis")

st.write("")



# ---------- INPUT BOX ----------

st.markdown('<div class="big-box">',unsafe_allow_html=True)

job_text = st.text_area(

"Paste Job Description",

height=250

)

st.markdown('</div>',unsafe_allow_html=True)



# ---------- PROCESS ----------

if job_text:

    cleaned = clean_text(job_text)

    st.session_state.job_text = cleaned

    skills = extract_skills(cleaned)


    st.success("Job Description Added")


    st.write("")


    st.subheader("Required Skills Detected")


    for skill in skills:

        st.markdown(
        f'<span class="skill-tag">{skill}</span>',
        unsafe_allow_html=True
        )

else:

    st.info("Paste Job Description to continue")