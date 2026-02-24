import streamlit as st


# PAGE CONFIG
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)


# ULTRA PREMIUM CSS DESIGN

st.markdown("""

<style>

/* Animated Background */

.stApp{

background: linear-gradient(-45deg,#020617,#0f172a,#111827,#1e293b);

background-size:400% 400%;

animation:gradient 18s ease infinite;

color:white;

}


@keyframes gradient{

0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}

}


/* Sidebar */

section[data-testid="stSidebar"]{

background:rgba(15,23,42,0.7);

backdrop-filter:blur(20px);

border-right:1px solid rgba(255,255,255,0.1);

}


/* Title */

.main-title{

font-size:70px;

font-weight:900;

background:linear-gradient(90deg,#22d3ee,#6366f1,#10b981);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

text-align:center;

}


/* Subtitle */

.subtitle{

color:#cbd5e1;

font-size:22px;

text-align:center;

}


/* Glass Card */

.glass{

background:rgba(255,255,255,0.05);

backdrop-filter:blur(20px);

border-radius:25px;

padding:40px;

margin-top:40px;

border:1px solid rgba(255,255,255,0.1);

box-shadow:0px 20px 60px rgba(0,0,0,0.7);

transition:0.3s;

}

.glass:hover{

transform:translateY(-5px);

}


/* Buttons */

.stButton>button{

background:linear-gradient(90deg,#22d3ee,#6366f1);

color:white;

border-radius:10px;

border:none;

padding:10px 25px;

font-weight:bold;

}


.stButton>button:hover{

box-shadow:0px 0px 20px #22d3ee;

}


/* Progress */

.stProgress > div > div > div{

background-image:linear-gradient(90deg,#22d3ee,#6366f1);

}


</style>

""",unsafe_allow_html=True)



# MAIN TITLE

st.markdown('<div class="main-title">🚀 AI Resume Analyzer</div>',unsafe_allow_html=True)

st.markdown('<div class="subtitle">Intelligent Job Matching System</div>',unsafe_allow_html=True)



st.write("")

st.write("")



# GLASS CARD

st.markdown("""

<div class="glass">

<h2>Welcome 👋</h2>

<p>

Upload your resume and job description to get:

<br><br>

✔ ATS Score<br>

✔ Skill Matching<br>

✔ Missing Skills<br>

✔ Resume Improvement Tips

</p>

</div>

""",unsafe_allow_html=True)



# SIDEBAR

st.sidebar.success("Navigate using sidebar")

st.sidebar.markdown("""

### Pages

📄 Resume Upload

📋 Job Description

📊 Analysis Dashboard

🎯 ATS Checker

""")