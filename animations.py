import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* ===== SOFT FUTURISTIC LIGHT BACKGROUND ===== */

.stApp{

background:

linear-gradient(
120deg,
#f7fbff,
#eef4ff,
#f9f6ff
);

}



/* ===== ANIME GLOW CIRCLES ===== */

.stApp::before{

content:"";

position:fixed;

width:500px;
height:500px;

top:-100px;
left:-100px;

background:

radial-gradient(
circle,
rgba(0,200,255,0.25),
transparent
);

filter:blur(80px);

animation:float1 12s infinite alternate;

}


.stApp::after{

content:"";

position:fixed;

width:400px;
height:400px;

bottom:-100px;
right:-100px;

background:

radial-gradient(
circle,
rgba(200,120,255,0.25),
transparent
);

filter:blur(80px);

animation:float2 12s infinite alternate;

}


@keyframes float1{

0%{transform:translateY(0px)}

100%{transform:translateY(80px)}

}


@keyframes float2{

0%{transform:translateY(0px)}

100%{transform:translateY(-80px)}

}


/* ===== GLASS CARDS ===== */

.card{

background:

rgba(255,255,255,0.75);

backdrop-filter:blur(20px);

padding:40px;

border-radius:20px;

box-shadow:

0px 20px 40px rgba(0,0,0,0.1);

transition:0.4s;

text-align:center;

}



/* ===== REAL 3D EFFECT ===== */

.card:hover{

transform:

rotateX(8deg)

rotateY(-8deg)

scale(1.05);

box-shadow:

0px 50px 80px rgba(0,0,0,0.2);

}


/* ===== TITLE GLOW ===== */

.title{

font-size:60px;

font-weight:800;

text-align:center;

background:

linear-gradient(
90deg,
#00c6ff,
#6a5cff
);

-webkit-background-clip:text;

-webkit-text-fill-color:transparent;

}


/* ===== SUBTITLE ===== */

.subtitle{

text-align:center;

font-size:22px;

color:#555;

}



/* ===== ROCKET ===== */

.rocket{

position:absolute;

top:40px;

left:-100px;

font-size:50px;

animation:rocketfly 12s infinite linear;

}


@keyframes rocketfly{

0%{
left:-100px;
}

100%{
left:110%;
}

}



/* ===== SIDEBAR PREMIUM ===== */

section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#ffffff,
#f2f6ff
);

box-shadow:

5px 0px 30px rgba(0,0,0,0.08);

}


/* Sidebar Animation */

section[data-testid="stSidebar"]:hover{

box-shadow:

10px 0px 50px rgba(0,0,0,0.15);

transition:0.3s;

}

</style>

""",unsafe_allow_html=True)



    st.markdown("""

<div class="rocket">
🚀
</div>

""",unsafe_allow_html=True)