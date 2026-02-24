import streamlit as st
from animations import load_animations

load_animations()

st.markdown('<div class="title">⭐ ATS Score</div>',unsafe_allow_html=True)


score=75

st.metric("ATS Score",score)

st.progress(score)