import streamlit as st
a = st.number_input('a:',0)
b = st.number_input('b',0)
c = a+b
st.write(c)

first, secound, third = st.columns(3)

with first:
    one = st.button('1')
    four = st.button('4')
    seven = st.button('7')
with secound:
    two = st.button('2')
    five = st.button('5')
    eight = st.button('8')
with third:
    three = st.button('3')
    six = st.button('6')
    nine = st.button('9')




