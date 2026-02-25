import streamlit as st
from animations import load_animations
from utils import extract_text_from_pdf

# Load Theme
load_animations()

# Hero Title
st.markdown("""
<div class="hero">
<h1>📄 Upload Resume</h1>
<p>Start Your AI Resume Analysis</p>
</div>
""",unsafe_allow_html=True)


st.write("")

st.subheader("Upload Resume PDF")

file = st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

if file:

    text = extract_text_from_pdf(file)

    st.session_state.resume_text = text

    st.success("Resume Uploaded Successfully ✅")

    st.write("")

    st.markdown("### Resume Preview")

    st.write(text[:1500])