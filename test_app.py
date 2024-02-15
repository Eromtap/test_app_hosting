import streamlit as st
import sqlalchemy

conn = st.connection("postgresql", type="sql")


df = conn.query('SELECT * FROM heart_rates;', ttl="0")

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
