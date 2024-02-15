import streamlit as st

conn = st.connection("postgresql", type="sql")


df = conn.query('SELECT * FROM hert_rates;', ttl="0")

for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
