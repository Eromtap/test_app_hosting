import streamlit as st
import psycopg2

CONNECT = psycopg2.connect(
    user = 'postgres',
    password = 'booger123',
    host = '34.171.140.16',
    port = 5432,
    database = 'summito2'
    )


st.write('app will live here... maybe')
