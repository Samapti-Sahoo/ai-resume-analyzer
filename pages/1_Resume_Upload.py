import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills


# ---------- PAGE TITLE ----------

st.title("📄 Resume Upload")

st.write("Upload your resume or use sample resume")

st.write("")


# ---------- DESIGN ----------

st.markdown("""

<style>

.upload-box{

background:rgba(255,255,255,0.05);

padding:30px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.1);

text-align:center;

}

.skill-tag{

background:rgba(16,185,129,0.3);

padding:8px 16px;

border-radius:20px;

margin:5px;

display:inline-block;

font-weight:bold;

}

</style>

""",unsafe_allow_html=True)



# ---------- FILE UPLOAD ----------

st.markdown('<div class="upload-box">',unsafe_allow_html=True)

uploaded_file = st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

st.markdown('</div>',unsafe_allow_html=True)



# ---------- SAMPLE RESUME BUTTON ----------

st.write("")

if st.button("Use Sample Resume"):

    sample_resume = """

Python developer with machine learning experience.

Skills include python, sql, machine learning,
data analysis, communication and problem solving.

"""

    st.session_state.resume_text = sample_resume

    st.success("Sample Resume Loaded")



# ---------- PROCESS PDF ----------

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    cleaned = clean_text(text)

    st.session_state.resume_text = cleaned


    skills = extract_skills(cleaned)


    st.success("Resume Uploaded Successfully")

    st.write("")


    st.subheader("Skills Detected")


    for skill in skills:

        st.markdown(
        f'<span class="skill-tag">{skill}</span>',
        unsafe_allow_html=True
        )


elif "resume_text" not in st.session_state:

    st.info("Upload Resume or Use Sample Resume")