import streamlit as st
import time


conn = st.connection("postgresql", type="sql")

pulse_1 = ''
pulse_2 = ''

empt = st.empty()

with empt: 
    while 1:
            df = conn.query('SELECT * FROM heart_rates;', ttl="0")
            for row in df.itertuples():
                p1 = row.pulse1
                p2 = row.pulse2
                if p1 != pulse_1 and p2 != pulse_2:
                    pulse_1 = p1
                    pulse_2 = p2
            st.write(pulse_1, pulse_2)
            time.sleep(2)







