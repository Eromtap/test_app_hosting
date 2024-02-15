import streamlit as st
import time

pulse_1, pulse_2 =st.columns(2)

numbers = st.empty()


for i in range(100):

    conn = st.connection("postgresql", type="sql")
        
    df = conn.query('SELECT * FROM heart_rates;', ttl="0")

    with pulse_1:    
        with numbers.container():
            st.write(df)
    with pulse_2:
        with numbers.container():
            st.write(df)        


    time.sleep(2)


st.write("hello")
