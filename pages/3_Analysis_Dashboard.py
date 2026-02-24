import streamlit as st
from animations import load_animations

load_animations()


st.markdown("""

<div class="title">

📊 Analysis Dashboard

</div>

""",unsafe_allow_html=True)



if "resume_text" not in st.session_state:

    st.warning("Upload Resume First")

    st.stop()



resume=st.session_state.resume_text
job=st.session_state.get("job_text","")



resume_skills=extract_skills(resume)
job_skills=extract_skills(job)



matched=list(set(resume_skills)&set(job_skills))
missing=list(set(job_skills)-set(resume_skills))



st.write("Matched:",matched)
st.write("Missing:",missing)