import streamlit as st
from animations import load_animations
from utils import extract_text_from_pdf

# Load 3D Theme
load_animations()


# HERO SECTION

st.markdown("""

<div class='hero'>

<h1>📄 Upload Resume</h1>

<p>Start Your AI Resume Analysis</p>

</div>

""",unsafe_allow_html=True)


st.write("")
st.write("")


# UPLOAD CARD

st.markdown("<div class='card'>",unsafe_allow_html=True)

file = st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

st.markdown("</div>",unsafe_allow_html=True)



if file:

    text = extract_text_from_pdf(file)

    st.session_state.resume_text = text

    st.success("Resume Uploaded Successfully")