import streamlit as st

st.set_page_config(
page_title="AI Resume Analyzer",
page_icon="🚀",
layout="wide"
)


# ---------- ANIME 3D BACKGROUND ----------

st.markdown("""

<style>

/* Anime Gradient Background */

.stApp {

background:

radial-gradient(circle at 20% 30%, #ff7eb3, transparent 40%),

radial-gradient(circle at 80% 70%, #65d6ff, transparent 40%),

linear-gradient(120deg,#0f2027,#203a43,#2c5364);

background-attachment:fixed;

color:white;

}



/* Floating Glow Animation */

@keyframes glowMove{

0%{background-position:0% 50%}

50%{background-position:100% 50%}

100%{background-position:0% 50%}

}



/* Title 3D */

.title{

font-size:75px;

font-weight:900;

text-align:center;

background:linear-gradient(90deg,#ffffff,#00ffd5,#65d6ff);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

text-shadow:

0px 5px 20px rgba(0,255,255,0.5);

}



/* Subtitle */

.subtitle{

text-align:center;

font-size:24px;

margin-bottom:60px;

color:#e2e8f0;

}



/* 3D Glass Cards */

.card{

background:rgba(255,255,255,0.07);

border-radius:30px;

padding:45px;

text-align:center;

backdrop-filter: blur(30px);

border:1px solid rgba(255,255,255,0.2);

box-shadow:

0px 25px 60px rgba(0,0,0,0.6),

inset 0px 2px 2px rgba(255,255,255,0.3);

transition:0.5s;

}



/* Hover Animation */

.card:hover{

transform:

translateY(-20px)

rotateX(5deg)

scale(1.05);

box-shadow:

0px 50px 100px rgba(0,0,0,0.9),

0px 0px 50px #00ffd5;

}



/* Card Title */

.card-title{

font-size:32px;

font-weight:800;

margin-top:10px;

}



/* Card Text */

.card-text{

color:#cbd5e1;

margin-top:10px;

font-size:18px;

}



/* Bottom Banner */

.bottom{

margin-top:60px;

padding:25px;

text-align:center;

border-radius:20px;

background:

linear-gradient(90deg,#ff7eb3,#65d6ff);

font-weight:bold;

font-size:20px;

color:black;

box-shadow:

0px 10px 40px rgba(0,0,0,0.6);

}

</style>

""",unsafe_allow_html=True)



# ---------- TITLE ----------

st.markdown(
'<div class="title">🚀 AI Resume Analyzer</div>',
unsafe_allow_html=True
)

st.markdown(
'<div class="subtitle">Next Generation AI Resume Matching System</div>',
unsafe_allow_html=True
)



# ---------- 3D CARDS ----------

col1,col2,col3=st.columns(3)


with col1:

    st.markdown("""

    <div class="card">

    <div style="font-size:60px">📄</div>

    <div class="card-title">

    Upload Resume

    </div>

    <div class="card-text">

    Analyze PDF Resume

    </div>

    </div>

    """,unsafe_allow_html=True)



with col2:

    st.markdown("""

    <div class="card">

    <div style="font-size:60px">🧠</div>

    <div class="card-title">

    AI Matching

    </div>

    <div class="card-text">

    Smart Skill Detection

    </div>

    </div>

    """,unsafe_allow_html=True)



with col3:

    st.markdown("""

    <div class="card">

    <div style="font-size:60px">📊</div>

    <div class="card-title">

    ATS Score

    </div>

    <div class="card-text">

    Resume Strength Analysis

    </div>

    </div>

    """,unsafe_allow_html=True)



# ---------- BOTTOM ----------

st.markdown("""

<div class="bottom">

Use Sidebar To Navigate

</div>

""",unsafe_allow_html=True)
