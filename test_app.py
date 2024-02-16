import streamlit as st
import asyncio
import time

st.set_page_config(layout="wide")

# def login():
#     pword = st.text_input('enter password', type="password")
#     if pword == 'booger123':
#         return 0
#     else:
#         return 1


def login():
    placeholder = st.empty()
    
    with placeholder.form("Login",clear_on_submit=True):
        pword = st.text_input("Entre Password: ")
        submitted = st.form_submit_button("Submit")
        if submitted and pword == 'booger123':
            placeholder.empty()
            return 0 
        else:
            return 1




st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    color: yellow;
    }
.medium-font {
    font-size:30px !important;
    color: green;
    }
</style>
""", unsafe_allow_html=True)


conn = st.connection("postgresql", type="sql")

left_maring, left, center, right, right_margin = st.columns([.1, .3, .2, .3, .1], gap='medium')

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



# placeholder = st.empty()

# with placeholder.form("login"):
#     st.markdown("#### Painel de Login")
#     email = st.text_input("Email", placeholder="Digite aqui seu email")
#     senha = st.text_input("Senha", placeholder="Digite aqui sua senha", type="password")
#     login_button = st.form_submit_button("Login")

#     if login_button:
#         placeholder.empty()

