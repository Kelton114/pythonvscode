import streamlit as st
st.title("Saving calculator")
sun = st.number_input("Please write down your saving for Sunday",0,value=0)
mon = st.number_input("Please write down your saving for Monday",0,value=0)
tues = st.number_input("Please write down your saving for Tuesday",0,value=0)
wend = st.number_input("Please write down your saving for Wenesday",0,value=0)
thurs = st.number_input("Please write down your saving for Thursday",0,value=0)
fri = st.number_input("Please write down your saving for Friday",0,value=0)
sat = st.number_input("Please write down your saving for Saturday",0,value=0)
if st.button("check you total saving"):
    st.write("You total saving from sunday to saturday is ", sun + mon + tues + wend + thurs + fri + sat,"dolars")