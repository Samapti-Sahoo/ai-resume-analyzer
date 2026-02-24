import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* ===== CINEMATIC BACKGROUND ===== */

.stApp{

background:

linear-gradient(
135deg,
#e6eeff,
#cfdcff,
#e8f0ff
);

}



/* ===== MAIN CONTAINER ===== */

.block-container{

background:

linear-gradient(
135deg,
rgba(30,40,80,0.95),
rgba(40,50,90,0.95)
);

padding:40px;

border-radius:25px;

box-shadow:
0px 20px 70px rgba(0,0,0,0.25);

color:white;

}



/* ===== TITLES ===== */

.title{

font-size:60px;

font-weight:bold;

text-align:center;

color:white;

letter-spacing:2px;

}


.subtitle{

text-align:center;

font-size:22px;

color:#dce6ff;

margin-bottom:30px;

}



/* ===== CINEMATIC CARDS ===== */

.card{

background:

rgba(255,255,255,0.1);

padding:50px;

border-radius:25px;

border:1px solid rgba(255,255,255,0.2);

text-align:center;

box-shadow:
0px 20px 40px rgba(0,0,0,0.3);

transition:0.4s;

cursor:pointer;

}



/* Hover */

.card:hover{

transform:

translateY(-15px)

scale(1.05);

box-shadow:
0px 40px 80px rgba(0,0,0,0.5);

}



/* Click Animation */

.card:active{

transform:scale(0.95);

}



/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#1b2a52,
#243870
);

color:white;

box-shadow:
5px 0px 30px rgba(0,0,0,0.3);

}



/* Sidebar Hover */

section[data-testid="stSidebar"]:hover{

box-shadow:
10px 0px 50px rgba(0,0,0,0.4);

}



/* Buttons Hidden Feel */

.stButton>button{

background:transparent;

border:none;

color:transparent;

height:0px;

}



/* METRIC STYLE */

[data-testid="metric-container"]{

background:

rgba(255,255,255,0.1);

padding:20px;

border-radius:15px;

border:1px solid rgba(255,255,255,0.2);

}



</style>

""",unsafe_allow_html=True)