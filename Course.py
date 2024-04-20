import streamlit as st
import pandas as pd
menu = st.sidebar.selectbox('Course',['Registration','Data'])

if menu == ('Registration'):
    st.header('Register here')
    one, two = st.columns(2)
    with one:
        st.write('')
        st.write('First Name')
        st.write('')
        st.write('Last Name')
        st.write('')

    with two:
        FN = st.text_input('First Name',label_visibility='collapsed',placeholder='First Name')
        LN = st.text_input('Last Name',label_visibility='collapsed',placeholder='Last Name')
    adress = st.text_input('Adress',placeholder='Adress')
    st.radio('Gender',['Male','Femail'])

    onee, twoo = st.columns(2)
    with onee:
        st.write('')
        st.write('Phone Number')        
        st.write('Email')
        st.write('')
        st.write('Password')
    with twoo:
        Phone = st.text_input('Phone',label_visibility='collapsed',placeholder='#### ####')
        Email = st.text_input('Email',label_visibility='collapsed',placeholder='Email')
        Password = st.text_input('Password',label_visibility='collapsed',placeholder='Password')
    st.button('Submit')