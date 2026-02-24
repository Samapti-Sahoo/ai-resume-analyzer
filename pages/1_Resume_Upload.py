import streamlit as st
from utils import extract_text_from_pdf, clean_text, extract_skills


# ---------- PAGE DESIGN ----------

st.markdown("""

<style>

/* Upload Box */

.upload-box{

background:rgba(255,255,255,0.05);

padding:40px;

border-radius:20px;

text-align:center;

border:1px solid rgba(255,255,255,0.1);

}


/* Skill Box */

.skill-box{

background:rgba(34,197,94,0.15);

padding:15px;

border-radius:10px;

margin:5px;

display:inline-block;

font-weight:bold;

}

</style>

""",unsafe_allow_html=True)



# ---------- TITLE ----------

st.markdown("# 📄 Resume Upload")

st.write("Upload Resume PDF for AI Analysis")

st.write("")



# ---------- UPLOAD AREA ----------

st.markdown('<div class="upload-box">',unsafe_allow_html=True)

uploaded_file = st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

st.markdown('</div>',unsafe_allow_html=True)



# ---------- PROCESS RESUME ----------

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    cleaned = clean_text(text)

    st.session_state.resume_text = cleaned


    skills = extract_skills(cleaned)


    st.success("Resume Uploaded Successfully")


    st.write("")


    st.subheader("Detected Skills")


    for skill in skills:

        st.markdown(
        f'<span class="skill-box">{skill}</span>',
        unsafe_allow_html=True
        )