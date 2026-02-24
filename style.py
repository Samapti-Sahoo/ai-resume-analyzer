def load_css():

    return """
<style>

/* Light Premium Background */

.stApp{

background: linear-gradient(
135deg,
#f8fbff,
#eef5ff,
#f5faff
);

}


/* Sidebar */

section[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#ffffff,
#f3f8ff
);

border-right:1px solid #d6e6ff;

box-shadow:0px 0px 20px rgba(0,0,0,0.05);

}


/* Title */

.title{

text-align:center;

font-size:52px;

font-weight:bold;

color:#0077ff;

}


/* Subtitle */

.subtitle{

text-align:center;

font-size:20px;

color:#555;

margin-bottom:30px;

}


/* Cards */

.card{

padding:40px;

border-radius:20px;

background:white;

border:1px solid #e5efff;

box-shadow:0px 10px 30px rgba(0,0,0,0.08);

transition:0.4s;

text-align:center;

}

.card:hover{

transform:translateY(-8px);

box-shadow:0px 25px 50px rgba(0,0,0,0.15);

}


/* Buttons */

.stButton>button{

background:#0077ff;

color:white;

border-radius:10px;

padding:10px 25px;

border:none;

}

.stButton>button:hover{

background:#005ce6;

}


/* Upload box */

.upload-box{

padding:30px;

border-radius:20px;

background:white;

border:2px dashed #0077ff;

box-shadow:0px 10px 25px rgba(0,0,0,0.08);

}


/* Metrics */

.metric{

padding:20px;

background:white;

border-radius:15px;

box-shadow:0px 10px 20px rgba(0,0,0,0.1);

text-align:center;

}

</style>
"""