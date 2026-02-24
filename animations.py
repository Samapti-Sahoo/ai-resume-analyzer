import streamlit as st

def load_animations():

    st.markdown("""
    <style>

    /* Animated Background */

    .stApp {
        background:
        radial-gradient(circle at 20% 30%, #e0f7ff 0%, transparent 40%),
        radial-gradient(circle at 80% 70%, #f0e6ff 0%, transparent 40%),
        linear-gradient(135deg,#f8fbff,#eef5ff);

        background-size: 200% 200%;
        animation: bgmove 12s infinite alternate;
    }

    @keyframes bgmove{
        0% {background-position:0% 50%;}
        100% {background-position:100% 50%;}
    }



    /* 3D CARDS */

    .card{

        background: white;

        padding:40px;

        border-radius:20px;

        box-shadow:
        0px 20px 40px rgba(0,0,0,0.15);

        transition:0.4s;

        text-align:center;

    }

    .card:hover{

        transform:

        rotateX(8deg)

        rotateY(-8deg)

        scale(1.05);

        box-shadow:
        0px 40px 80px rgba(0,0,0,0.25);

    }


    /* ROCKET ANIMATION */

    .rocket{

        position:absolute;

        top:50px;

        left:-100px;

        font-size:60px;

        animation:rocketfly 10s infinite linear;

    }

    @keyframes rocketfly{

        0%{
        left:-100px;
        transform:rotate(-10deg)
        }

        50%{
        transform:rotate(5deg)
        }

        100%{
        left:110%;
        transform:rotate(-10deg)
        }

    }


    /* SIDEBAR PREMIUM */

    section[data-testid="stSidebar"]{

        background:linear-gradient(
        180deg,
        #f0f6ff,
        #ffffff
        );

        box-shadow:
        5px 0px 25px rgba(0,0,0,0.1);

    }


    </style>
    """,unsafe_allow_html=True)



    st.markdown("""
    <div class="rocket">
    🚀
    </div>
    """,unsafe_allow_html=True)