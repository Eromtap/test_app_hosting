import streamlit as st
import time




conn = st.connection("postgresql", type="sql")

# pulse_1 = ''
# pulse_2 = ''

# empt = st.empty()


st.markdown("#### Pulse Rate 1:")
numbers = st.empty()

for i in range(0,10):
    df = conn.query('SELECT * FROM heart_rates;', ttl="0")
    for row in df.itertuples():
        p1 = row.pulse1
        p2 = row.pulse2
    with numbers.container():
      st.write(p1)
      st.write(p2)
      time.sleep(1)







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


