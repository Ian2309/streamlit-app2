import streamlit as st

st.title("My Streamlit Web App")

name = st.text_input("Enter your name")

if name:
    st.write("Hello", name)