import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* Background */

.stApp{

background:linear-gradient(
135deg,
#3a3f6b,
#2c2f55,
#1f2240
);

color:#ffffff;

}


/* Title */

.title{

text-align:center;

font-size:70px;

font-weight:800;

color:#ffffff;

text-shadow:0px 0px 30px cyan;

}


.subtitle{

text-align:center;

font-size:24px;

color:#d7e0ff;

margin-bottom:40px;

}



/* Rocket */

.rocket{

font-size:70px;

text-align:center;

animation:fly 3s infinite;

}


@keyframes fly{

0%{transform:translateY(0px)}
50%{transform:translateY(-15px)}
100%{transform:translateY(0px)}

}



/* Cards */

.card{

background:rgba(255,255,255,0.08);

padding:40px;

border-radius:25px;

text-align:center;

backdrop-filter:blur(10px);

box-shadow:
0px 10px 30px rgba(0,0,0,0.5);

transition:0.4s;

cursor:pointer;

height:260px;

}


/* Card Text */

.card h1{

font-size:50px;

}


.card h2{

color:#ffffff;

font-size:28px;

}


.card p{

color:#cfd8ff;

font-size:18px;

}



.card:hover{

transform:
scale(1.07)
translateY(-10px);

box-shadow:
0px 20px 50px rgba(0,0,0,0.8);

}



/* Sidebar */

section[data-testid="stSidebar"]{

background:linear-gradient(

180deg,
#23264a,
#3a3f6b

);

}


section[data-testid="stSidebar"] *{

color:#ffffff !important;

}



/* Buttons */

.stButton>button{

background:linear-gradient(

90deg,
#00c6ff,
#0072ff

);

border:none;

border-radius:20px;

padding:15px;

color:white;

font-size:18px;

transition:0.3s;

}


.stButton>button:hover{

transform:scale(1.1);

}


</style>

""",unsafe_allow_html=True)