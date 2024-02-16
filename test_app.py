import streamlit as st
import asyncio
import time


st.set_page_config(layout="wide")
conn = st.connection("postgresql", type="sql")
left_margin, left, center, right, right_margin = st.columns([.1, .3, .2, .3, .1], gap='medium')

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Anton&family=Outfit:wght@100..900&display=swap')
</style>
<style>
.big-font {
    font-size:70px !important;
    color: yellow;
    }
.medium-font {
    font-family: "Outfit", sans-serif;
    font-weight: 200;
    font-size:50px !important;
    color: green;
    }
</style>
""", unsafe_allow_html=True)

# simple password login. Password in plain text. Yeah, I know... But this is mainly just to keep
# random people from accessing the app and hitting the database a ton. Not really for serious security
# could add hashing and check against database for login but i don't wanna
def login():
    with center:
        placeholder = st.empty()

        with placeholder.form("Login",clear_on_submit=True):
            pword = st.text_input("Entre Password: ", type="password")
            submitted = st.form_submit_button("Submit")
            if submitted and pword == 'booger123':
                placeholder.empty()
                return 0 
            else:
                return 1


async def left_col():
    with left:
        st.markdown('<p class="big-font">Pulse Rate 1:</p>', unsafe_allow_html=True)
        numbers = st.empty()
        
        
        while 1:
            df = conn.query('SELECT * FROM heart_rates;', ttl="0")
            for row in df.itertuples():
                p1 = row.pulse1
            with numbers.container():
              st.markdown(f'<p class="medium-font">{p1}</p>', unsafe_allow_html=True)
              await asyncio.sleep(1)

async def right_col():
    with right:
        st.markdown('<p class="big-font">Pulse Rate 2:</p>', unsafe_allow_html=True)
        numbers = st.empty()
        
        
        while 1:
            df = conn.query('SELECT * FROM heart_rates;', ttl="0")
            for row in df.itertuples():
                p2 = row.pulse2
            with numbers.container():
              st.markdown(f'<p class="medium-font">{p2}</p>', unsafe_allow_html=True)
              await asyncio.sleep(1)



async def main():
    if login() == 0:
        await asyncio.gather(right_col(), left_col())
    


asyncio.run(main())





