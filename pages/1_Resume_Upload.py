import streamlit as st
from animations import load_animations
from utils import extract_text_from_pdf

# Load Cinematic Theme
load_animations()


# Title

st.markdown(
'<div class="title">📄 Resume Upload</div>',
unsafe_allow_html=True
)


st.markdown(
'<div class="subtitle">Upload Resume For AI Analysis</div>',
unsafe_allow_html=True
)



# Upload Box

st.markdown('<div class="card">',unsafe_allow_html=True)

file = st.file_uploader(
"Upload Resume PDF",
type=["pdf"]
)

st.markdown('</div>',unsafe_allow_html=True)



# Process Resume

if file:

    text = extract_text_from_pdf(file)

    st.session_state.resume_text = text

    st.success("Resume Uploaded Successfully ✅")


    st.markdown("""

<div class="card">

<h3>Resume Ready For Analysis</h3>

Go To Analysis Dashboard →

</div>

""",unsafe_allow_html=True)