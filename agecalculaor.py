#create an age calculator to ask the name, year of birth and currecnt year to find the age
import streamlit as st
st.title("Age calculator")
name = st.text_input("Please write your name")
yob = st.number_input("Please enter you year of birth",1930,value=1930)
cy = st.number_input("Please enter the current year",2023,value=2023)
age = cy - yob
if st.button("Check your age"):
    st.write(name,",you are ",age," years old")