import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* ===== BACKGROUND ===== */

.stApp{

background:

linear-gradient(
135deg,
#edf3ff,
#dbe6ff,
#edf3ff
);

}



/* ===== MAIN CONTAINER ===== */

.block-container{

background:

linear-gradient(
135deg,
rgba(30,40,80,0.9),
rgba(40,60,110,0.9)
);

padding:40px;

border-radius:20px;

box-shadow:
0px 20px 60px rgba(0,0,0,0.2);

color:white;

}



/* ===== TITLE ===== */

.title{

font-size:55px;
font-weight:bold;
text-align:center;
color:white;

}



/* ===== SUBTITLE ===== */

.subtitle{

text-align:center;
font-size:22px;
color:#e3ecff;

}



/* ===== CARDS ===== */

.card{

background:
rgba(255,255,255,0.12);

padding:40px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.2);

box-shadow:
0px 15px 40px rgba(0,0,0,0.3);

transition:0.3s;

text-align:center;

color:white;

}


.card:hover{

transform:translateY(-10px);

box-shadow:
0px 40px 70px rgba(0,0,0,0.5);

}



/* ===== BUTTONS ===== */

.stButton>button{

background:#3b6cff;
color:white;
border-radius:10px;

}



/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#1e2a4a,
#2c3c6b
);

color:white;

}



</style>

""",unsafe_allow_html=True)