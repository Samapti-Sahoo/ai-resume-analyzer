import streamlit as st
from utils import extract_text_from_pdf
from style import load_css


st.markdown(load_css(),unsafe_allow_html=True)

st.title("📄 Upload Resume")


st.markdown('<div class="upload-box">',unsafe_allow_html=True)

file=st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

st.markdown('</div>',unsafe_allow_html=True)



if file:

    text=extract_text_from_pdf(file)

    st.session_state.resume_text=text

    st.success("Resume Uploaded Successfully")