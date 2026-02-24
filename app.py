import streamlit as st

st.set_page_config(
page_title="AI Resume Analyzer",
page_icon="🚀",
layout="wide"
)

# -------- INSANE ANIME BACKGROUND --------

st.markdown("""

<style>

/* Animated Anime Sky */

.stApp{

background:

radial-gradient(circle at 10% 20%, #ff00cc55, transparent 40%),

radial-gradient(circle at 90% 80%, #00ffee55, transparent 40%),

linear-gradient(140deg,#050a30,#000428,#004e92);

background-size:400% 400%;

animation:bgmove 15s infinite;

color:white;

}


@keyframes bgmove{

0%{background-position:0% 50%}

50%{background-position:100% 50%}

100%{background-position:0% 50%}

}



/* Floating Lights */

.stApp::before{

content:"";

position:fixed;

width:100%;

height:100%;

background-image:

radial-gradient(white 1px, transparent 1px);

background-size:50px 50px;

opacity:0.15;

animation:stars 60s linear infinite;

z-index:-1;

}


@keyframes stars{

0%{transform:translateY(0px)}

100%{transform:translateY(-2000px)}

}



/* Neon Title */

.title{

font-size:80px;

font-weight:900;

text-align:center;

background:linear-gradient(90deg,#00ffd5,#ffffff,#00ffd5);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

text-shadow:

0px 0px 20px #00ffd5,

0px 0px 40px #00ffd5,

0px 0px 60px #00ffd5;

}



/* Subtitle */

.subtitle{

text-align:center;

font-size:26px;

margin-bottom:60px;

color:#d1d5db;

}



/* INSANE 3D CARDS */

.card{

background:rgba(255,255,255,0.05);

border-radius:35px;

padding:60px;

text-align:center;

backdrop-filter: blur(40px);

border:1px solid rgba(255,255,255,0.2);

box-shadow:

0px 30px 80px rgba(0,0,0,0.8),

inset 0px 3px 5px rgba(255,255,255,0.3);

transition:0.6s;

transform-style:preserve-3d;

}



/* Hover 3D */

.card:hover{

transform:

rotateX(10deg)

rotateY(10deg)

scale(1.08)

translateY(-20px);

box-shadow:

0px 80px 150px rgba(0,0,0,1),

0px 0px 80px #00ffd5;

}



/* Card Title */

.card-title{

font-size:34px;

font-weight:900;

margin-top:15px;

}



/* Card Text */

.card-text{

font-size:18px;

margin-top:10px;

color:#cbd5e1;

}



/* Floating Animation */

.float{

animation:float 4s ease-in-out infinite;

}

@keyframes float{

0%{transform:translateY(0px)}

50%{transform:translateY(-15px)}

100%{transform:translateY(0px)}

}



/* Bottom Banner */

.bottom{

margin-top:70px;

padding:30px;

text-align:center;

border-radius:25px;

background:

linear-gradient(90deg,#ff00cc,#00ffee);

font-weight:bold;

font-size:22px;

color:black;

box-shadow:

0px 20px 60px rgba(0,0,0,0.8);

animation:glow 3s infinite alternate;

}

@keyframes glow{

from{box-shadow:0px 0px 20px #00ffee}

to{box-shadow:0px 0px 60px #ff00cc}

}

</style>

""",unsafe_allow_html=True)



# -------- TITLE --------

st.markdown(

'<div class="title float">🚀 AI Resume Analyzer</div>',

unsafe_allow_html=True

)

st.markdown(

'<div class="subtitle">Futuristic AI Resume Intelligence System</div>',

unsafe_allow_html=True

)



# -------- 3D CARDS --------

col1,col2,col3=st.columns(3)



with col1:

 st.markdown("""

 <div class="card float">

 <div style="font-size:70px">

 📄

 </div>

 <div class="card-title">

 Upload Resume

 </div>

 <div class="card-text">

 Smart Resume Parser

 </div>

 </div>

 """,unsafe_allow_html=True)



with col2:

 st.markdown("""

 <div class="card float">

 <div style="font-size:70px">

 🧠

 </div>

 <div class="card-title">

 AI Matching

 </div>

 <div class="card-text">

 Deep Skill Detection

 </div>

 </div>

 """,unsafe_allow_html=True)



with col3:

 st.markdown("""

 <div class="card float">

 <div style="font-size:70px">

 📊

 </div>

 <div class="card-title">

 ATS Score

 </div>

 <div class="card-text">

 Resume Intelligence

 </div>

 </div>

 """,unsafe_allow_html=True)



# -------- BOTTOM --------

st.markdown("""

<div class="bottom">

Use Sidebar To Navigate 🚀

</div>

""",unsafe_allow_html=True)