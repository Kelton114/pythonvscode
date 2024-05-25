#Create a an Arithmetic Calculator that performs addition, subtraction, division and multiplication operation between two numbers.

#Ensure to add an image and also make use of buttons ‘+’, ‘-‘, ‘/‘, and ‘*’.

import streamlit as st
st.set_page_config(layout='wide')
st.header('Calculator')
math = st.write('')
ein, zwei, drei, vier = st.columns(4)
with ein:
    seven = st.button('7')
    if seven:
        digit = '7'
    four = st.button('4')
    if four:
        digit = '4'
    one = st.button('1')
    if one:
        digit = '1'
with zwei:
    eight = st.button('8')
    if eight:
        digit = '8'
    five = st.button('5')
    if five:
        digit = '5'
    two = st.button('2')
    if two:
        digit = '2'
with drei:
    nine = st.button('9')
    if nine:
        digit = '9'
    six = st.button('6')
    if six:
        digit = '6'
    three = st.button('3')
    if three:
        digit = '3'
with vier:
    minus = st.button('-')
    plus = st.button('+')
    times = st.button('*')

if one or two or three or four or five or six or seven or eight or nine:
    number = ''
    newnumber = number + digit
    number = newnumber
    st.write(newnumber+digit)