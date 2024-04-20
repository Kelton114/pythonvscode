import streamlit as st

st.title("Wecome")
st.header("To my addition page")
st.subheader("It is my first page on python")

name = st.text_input("Enter your name")

a = st.number_input('Enter your first number',0,500,value=0,step=10)

b = st.number_input('Enter your second number',0,500,value=0,step=10)

c = a + b

if st.checkbox("Are you allowed to use the internet"):
    st.write("The addition is",c)
if st.button("Check Addition"):
    st.write("The addition is",c)