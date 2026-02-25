import streamlit as st
from animations import load_animations


load_animations()


st.markdown("""

<div class="hero">

<h1>📈 ATS Checker</h1>

<p>Check Resume Strength</p>

</div>

""",unsafe_allow_html=True)



if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()



resume = st.session_state.resume_text


length = len(resume)


score = min(100,int(length/40))


st.markdown("## ATS Score")

st.metric("ATS Compatibility",f"{score}%")


st.progress(score)



if score > 75:

    st.success("Strong Resume")

elif score > 50:

    st.warning("Moderate Resume")

else:

    st.error("Weak Resume")