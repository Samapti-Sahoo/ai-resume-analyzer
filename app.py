import streamlit as st

# Page Config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)

# Ultra Professional CSS Design

st.markdown("""
<style>

/* Animated Background */

.stApp {
background: linear-gradient(-45deg,#0f172a,#111827,#1e293b,#020617);
background-size:400% 400%;
animation:gradient 15s ease infinite;
color:white;
}

@keyframes gradient{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:rgba(30,41,59,0.8);
backdrop-filter:blur(10px);
}

/* Big Title */

.main-title{
font-size:60px;
font-weight:800;
background:linear-gradient(90deg,#6366f1,#22d3ee,#10b981);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* Subtitle */

.subtitle{
color:#cbd5e1;
font-size:22px;
}

/* Glass Cards */

.glass{

background:rgba(255,255,255,0.05);
backdrop-filter:blur(10px);

border-radius:20px;

padding:30px;

margin:10px;

border:1px solid rgba(255,255,255,0.1);

box-shadow:0px 10px 30px rgba(0,0,0,0.4);

}

</style>
""",unsafe_allow_html=True)

# Landing Page

st.markdown('<div class="main-title">AI Resume Analyzer</div>',unsafe_allow_html=True)

st.markdown('<div class="subtitle">AI Powered Resume Intelligence System</div>',unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)

col1,col2,col3=st.columns(3)

with col1:

 st.markdown("""
 <div class="glass">
 <h3>📄 Resume Upload</h3>
 Upload PDF Resume and extract skills
 </div>
 """,unsafe_allow_html=True)


with col2:

 st.markdown("""
 <div class="glass">
 <h3>🧠 Smart Matching</h3>
 AI compares resume with job description
 </div>
 """,unsafe_allow_html=True)


with col3:

 st.markdown("""
 <div class="glass">
 <h3>📊 ATS Score</h3>
 Get compatibility score instantly
 </div>
 """,unsafe_allow_html=True)

st.sidebar.success("Navigate using sidebar")