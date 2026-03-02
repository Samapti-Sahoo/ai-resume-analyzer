import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* SIDEBAR REMOVE */

section[data-testid="stSidebar"]{
display:none;
}

div[data-testid="collapsedControl"]{
display:none;
}


/* APP BACKGROUND */

.stApp{

background:

linear-gradient(
180deg,
#e8edf7,
#dfe6f3
);

font-family:sans-serif;

}



/* NAVBAR */

.navbar{

position:fixed;

top:0;

left:0;

right:0;

height:70px;

background:white;

box-shadow:0px 5px 20px rgba(0,0,0,0.1);

display:flex;

align-items:center;

justify-content:space-between;

padding-left:40px;

padding-right:40px;

z-index:999;

}


/* LOGO */

.logo{

font-size:28px;

font-weight:bold;

color:#111;

}



/* NAV LINKS */

.nav-links a{

margin-left:30px;

text-decoration:none;

font-size:18px;

color:#333;

font-weight:500;

}


.nav-links a:hover{

color:#007bff;

}



/* HERO */

.hero{

margin-top:120px;

text-align:center;

}


.hero h1{

font-size:55px;

color:#111;

}


.hero p{

font-size:22px;

color:#444;

}



/* CARDS */

.card{

background:white;

padding:40px;

border-radius:25px;

box-shadow:

0px 20px 40px rgba(0,0,0,0.15);

text-align:center;

}



.card:hover{

transform:translateY(-8px);

transition:0.3s;

}



/* GRID */

.grid{

display:grid;

grid-template-columns:1fr 1fr 1fr;

gap:30px;

margin-top:40px;

}



/* BUTTON */

.btn{

margin-top:20px;

padding:12px 20px;

background:black;

color:white;

border-radius:10px;

display:inline-block;

text-decoration:none;

}

</style>

""",unsafe_allow_html=True)