import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* ===== MEDIUM DARK BACKGROUND ===== */

.stApp{

background:

linear-gradient(
135deg,
#eaf2ff,
#dfe9ff,
#edf3ff
);

color:#111;

}



/* ===== SOFT DARK CONTAINER ===== */

.block-container{

background:

linear-gradient(
135deg,
rgba(40,60,100,0.85),
rgba(30,40,80,0.85)
);

padding:40px;

border-radius:20px;

box-shadow:

0px 20px 60px rgba(0,0,0,0.2);

color:white;

}



/* ===== TITLE ===== */

.title{

font-size:60px;

font-weight:800;

text-align:center;

color:white;

}



/* ===== SUBTITLE ===== */

.subtitle{

text-align:center;

font-size:22px;

color:#dfe8ff;

}



/* ===== GLASS CARDS ===== */

.card{

background:

rgba(255,255,255,0.12);

padding:40px;

border-radius:20px;

border:1px solid rgba(255,255,255,0.2);

box-shadow:

0px 15px 40px rgba(0,0,0,0.3);

transition:0.4s;

text-align:center;

color:white;

}



/* ===== 3D HOVER ===== */

.card:hover{

transform:

translateY(-10px)

scale(1.04);

box-shadow:

0px 40px 70px rgba(0,0,0,0.5);

}



/* ===== ROCKET ===== */

.rocket{

position:absolute;

top:20px;

left:-100px;

font-size:50px;

animation:rocketfly 15s infinite linear;

}


@keyframes rocketfly{

0%{left:-100px;}

100%{left:110%;}

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



    st.markdown("""

<div class="rocket">

🚀

</div>

""",unsafe_allow_html=True)