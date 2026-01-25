import streamlit as st

st.title("IST 488 - Labs and Homework")

lab1_page = st.Page("Lab1.py", title="Lab 1", icon="🔬")
hw1_page = st.Page("HW1.py", title="Homework 1", icon="📝")

pg = st.navigation([lab1_page, hw1_page])
pg.run()

