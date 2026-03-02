import streamlit as st
from animations import load_animations
from utils import clean_text


load_animations()


st.markdown("""

<div class='hero'>

<h1>📝 Job Description</h1>

<p>Tell AI About Your Target Job</p>

</div>

""",unsafe_allow_html=True)


st.write("")
st.write("")


st.markdown("<div class='card'>",unsafe_allow_html=True)

job_text = st.text_area(
"Paste Job Description",
height=250
)

st.markdown("</div>",unsafe_allow_html=True)



if job_text:

    cleaned = clean_text(job_text)

    st.session_state.job_text = cleaned

    st.success("Job Description Added Successfully")