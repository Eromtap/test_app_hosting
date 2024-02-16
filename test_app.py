import streamlit as st
import asyncio
import time

st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    color: yellow;
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
              st.markdown('<p class="big-font">Pulse Rate 1:</p>', unsafe_allow_html=True)
              #st.write(p1)
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
              st.write(p2)
              await asyncio.sleep(1)



async def main():
    await asyncio.gather(right_col(), left_col())
    


asyncio.run(main())


# while 1:
#     df = conn.query('SELECT * FROM heart_rates;', ttl="0")
#     for row in df.itertuples():
#         p1 = row.pulse1
#         p2 = row.pulse2
#     with pulse1:
#         pulse1.empty()
#         st.write(p1)

#     with pulse2:
#         st.empty()
#         st.write(p2)
    
#     time.sleep(2)




# st.markdown("#### Numbers overwriting each other")
# numbers = st.empty()

# for i in range(0,10):
#     with numbers.container():
#       st.write(i)
#       time.sleep(1)


