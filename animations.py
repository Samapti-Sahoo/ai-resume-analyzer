import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* CINEMATIC BACKGROUND */

.stApp{

background:
radial-gradient(circle at 20% 30%, rgba(255,255,255,0.4), transparent 40%),
radial-gradient(circle at 80% 60%, rgba(200,220,255,0.4), transparent 40%),
linear-gradient(
180deg,
#e9edf7,
#cfd6ea
);

animation:bgmove 12s infinite alternate;

}



@keyframes bgmove{

0%{
background-position:0% 0%;
}

100%{
background-position:100% 100%;
}

}



/* HERO TITLE */

.hero{

text-align:center;

padding-top:40px;

animation:fadeup 1s;

}


.hero h1{

font-size:60px;

color:#111;

text-shadow:0px 5px 15px rgba(0,0,0,0.2);

}


.hero p{

font-size:22px;

color:#333;

}



/* FLOATING GLOW */

.hero h1::after{

content:"";

position:absolute;

width:200px;

height:200px;

background:rgba(100,150,255,0.2);

filter:blur(80px);

left:50%;

top:80px;

transform:translateX(-50%);

animation:float 6s infinite;

}



@keyframes float{

0%{transform:translate(-50%,0px)}

50%{transform:translate(-50%,20px)}

100%{transform:translate(-50%,0px)}

}



/* CARDS */

.card{

background:white;

padding:30px;

border-radius:18px;

box-shadow:
0px 10px 30px rgba(0,0,0,0.15);

transition:0.4s;

cursor:pointer;

}



.card:hover{

transform:

translateY(-10px)
scale(1.03);

box-shadow:

0px 20px 50px rgba(0,0,0,0.25);

}



/* FILE UPLOADER */

[data-testid="stFileUploader"]{

background:white;

padding:20px;

border-radius:15px;

box-shadow:0px 5px 20px rgba(0,0,0,0.1);

}



/* SIDEBAR CINEMATIC */

section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#34436b,
#2a3454
);

color:white;

}



/* PAGE ENTRY */

section.main{

animation:fadeup 1s;

}



@keyframes fadeup{

from{

opacity:0;
transform:translateY(40px);

}

to{

opacity:1;
transform:translateY(0px);

}

}



/* TEXT VISIBILITY */

h1,h2,h3,h4{

color:#111 !important;

}

p{

color:#222 !important;

}

label{

color:#111 !important;

}

</style>

""",unsafe_allow_html=True)