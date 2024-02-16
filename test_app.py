import streamlit as st
import time

pulse1, pulse2 = st.columns(2)


conn = st.connection("postgresql", type="sql")

pulse_1 = ''
pulse_2 = ''

empt = st.empty()


while 1:
    df = conn.query('SELECT * FROM heart_rates;', ttl="0")
    for row in df.itertuples():
        p1 = row.pulse1
        p2 = row.pulse2
    with pulse1:
        pulse1.empty()
        st.write(p1)

    with pulse2:
        st.empty()
        st.write(p2)
    
    time.sleep(2)







