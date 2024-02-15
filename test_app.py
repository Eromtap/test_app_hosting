import streamlit as st
import time


numbers = st.empty()

for i in range(100):
    conn = st.connection("postgresql", type="sql")
        
    df = conn.query('SELECT * FROM heart_rates;', ttl="0")

    with numbers.container():
        st.write(df)



    time.sleep(2)


st.write("hello")
