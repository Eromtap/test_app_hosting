import streamlit as st
import time



for i in range(100):
    conn = st.connection("postgresql", type="sql")
        
    df = conn.query('SELECT * FROM heart_rates;', ttl="0")
    
    for row in df.itertuples():
        st.write(f"{row.pulse1} has a :{row.pulse2}:")


st.write("hello")
