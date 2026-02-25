import streamlit as st

def load_animations():

    st.markdown("""

<style>

/* Background Medium Light Theme */

body{

background:linear-gradient(
180deg,
#e9edf7,
#cfd6ea
);

font-family:Segoe UI;

}



/* Hero Title */

.hero{

text-align:center;

padding:40px;

}



.hero h1{

font-size:55px;

color:#111111;

}



.hero p{

font-size:20px;

color:#333333;

}



/* Upload Box */

[data-testid="stFileUploader"]{

background:#ffffff;

padding:20px;

border-radius:12px;

box-shadow:0px 5px 20px rgba(0,0,0,0.1);

}



/* Buttons */

button{

height:65px !important;

font-size:18px !important;

border-radius:12px !important;

}



/* Sidebar */

section[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#2f3b5c,
#222c46
);

color:white;

}



/* Fade Animation */

section.main{

animation:fade 0.8s;

}



@keyframes fade{

from{

opacity:0;

transform:translateY(40px);

}

to{

opacity:1;

transform:translateY(0px);

}

}



/* Text Visibility Fix */

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