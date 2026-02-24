import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# ---------- PREMIUM CSS ----------
st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#0f172a,#020617);
color:white;
}

/* Remove Streamlit menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Title */
.big-title{
font-size:60px;
font-weight:bold;
text-align:center;
background: linear-gradient(90deg,#22c55e,#38bdf8);
-webkit-background-clip:text;
color:transparent;
}

.subtitle{
text-align:center;
font-size:22px;
color:#cbd5e1;
margin-bottom:30px;
}

/* Cards */

.card{
background:rgba(255,255,255,0.05);
padding:30px;
border-radius:20px;
text-align:center;
border:1px solid rgba(255,255,255,0.1);
transition:0.3s;
}

.card:hover{
transform:translateY(-10px);
background:rgba(255,255,255,0.08);
}

.metric{

font-size:35px;
font-weight:bold;
color:#22c55e;

}

</style>
""", unsafe_allow_html=True)


# ---------- HEADER ----------

st.markdown('<div class="big-title">🚀 AI Resume Analyzer</div>',unsafe_allow_html=True)

st.markdown(
'<div class="subtitle">Intelligent Resume Matching System</div>',
unsafe_allow_html=True
)

st.write("")
st.write("")


# ---------- CARDS ----------

col1,col2,col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="card">
    📄
    <h2>Upload Resume</h2>
    Analyze PDF Resume
    </div>
    """,unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">
    🧠
    <h2>AI Matching</h2>
    Smart Skill Detection
    </div>
    """,unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="card">
    📊
    <h2>ATS Score</h2>
    Resume Strength
    </div>
    """,unsafe_allow_html=True)



st.write("")
st.write("")
st.write("")

st.success("Use Sidebar To Navigate")