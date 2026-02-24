import streamlit as st

def load_animations():

    st.markdown("""

<style>

body{
background:linear-gradient(135deg,#dfe9f3,#f5f7fa);
}


/* Title */

.title{
text-align:center;
font-size:60px;
font-weight:800;
color:#243b55;
animation:fade 2s;
}

.subtitle{
text-align:center;
font-size:22px;
color:#4a5a70;
margin-bottom:40px;
animation:fade 3s;
}


/* Cards */

.card{

background:linear-gradient(145deg,#ffffff,#e6ecf5);

padding:40px;

border-radius:25px;

text-align:center;

box-shadow:

10px 10px 20px rgba(0,0,0,0.15),

-10px -10px 20px white;

transition:0.4s;

cursor:pointer;

height:250px;

}


.card:hover{

transform:

translateY(-10px)

scale(1.05);

box-shadow:

0px 20px 40px rgba(0,0,0,0.3);

}



/* Sidebar */

section[data-testid="stSidebar"]{

background:

linear-gradient(

180deg,

#2c3e50,

#4ca1af

);

color:white;

}



section[data-testid="stSidebar"] *{

color:white !important;

}



/* Cinematic Button */

.stButton>button{

background:linear-gradient(

90deg,

#36d1dc,

#5b86e5

);

border:none;

padding:14px;

border-radius:20px;

color:white;

font-size:18px;

transition:0.4s;

}



.stButton>button:hover{

transform:scale(1.1);

}


/* Rocket Animation */

.rocket{

font-size:60px;

animation:fly 3s infinite;

text-align:center;

}


@keyframes fly{

0%{transform:translateY(0px)}

50%{transform:translateY(-20px)}

100%{transform:translateY(0px)}

}


/* Fade */

@keyframes fade{

from{opacity:0}

to{opacity:1}

}

</style>

""",unsafe_allow_html=True)