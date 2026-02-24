import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* MAIN BACKGROUND */

.stApp{

background:linear-gradient(
135deg,
#3c4172,
#2c2f55,
#1b1e3f
);

font-family:Segoe UI;

color:#ffffff;

}



/* FORCE ALL TEXT VISIBLE */

p,span,label,div{

color:#ffffff !important;

}


h1,h2,h3{

color:#ffffff !important;

}


/* Streamlit Text Fix */

.stMarkdown{

color:white !important;

}

.stText{

color:white !important;

}

.stSubheader{

color:white !important;

}

.stTitle{

color:white !important;

}

.stHeader{

color:white !important;

}



/* INPUT TEXT */

textarea{

color:black !important;

background:white !important;

}


input{

color:black !important;

background:white !important;

}



/* TITLE */

.title{

text-align:center;

font-size:70px;

font-weight:800;

color:white;

text-shadow:0px 0px 30px cyan;

}


.subtitle{

text-align:center;

font-size:24px;

color:#e8ecff;

margin-bottom:40px;

}



/* ROCKET */

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



/* CARDS */

.card{

background:rgba(255,255,255,0.12);

padding:40px;

border-radius:25px;

text-align:center;

backdrop-filter:blur(12px);

box-shadow:

0px 10px 30px rgba(0,0,0,0.6);

transition:0.4s;

cursor:pointer;

height:260px;

}



/* CARD TEXT */

.card h1{

font-size:50px;

color:white;

}


.card h2{

font-size:30px;

color:white;

}


.card p{

font-size:18px;

color:#e6ecff;

}



/* HOVER */

.card:hover{

transform:
scale(1.08)
translateY(-10px);

box-shadow:
0px 20px 60px rgba(0,0,0,0.9);

}



/* SIDEBAR */

section[data-testid="stSidebar"]{

background:linear-gradient(

180deg,
#25285a,
#3c4172

);

}


section[data-testid="stSidebar"] *{

color:white !important;

}



/* BUTTONS */

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



/* SUCCESS BOX */

.stAlert{

color:white !important;

}



/* METRIC TEXT */

[data-testid="stMetricValue"]{

color:white !important;

}


[data-testid="stMetricLabel"]{

color:#e8ecff !important;

}



/* PROGRESS TEXT */

.stProgress{

color:white !important;

}



/* WARNING */

.stWarning{

color:white !important;

}



</style>

""",unsafe_allow_html=True)