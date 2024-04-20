import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

adminpassword = '12345'

pass1,pass2 = st.sidebar.columns(2)

with pass1:
    password = st.sidebar.text_input('Enter the admin password',type='password')
    passwordbutton = st.sidebar.button('Login')

if passwordbutton:
    if password:
        if password == adminpassword:
            df = pd.read_csv('employeedb1.csv')
            st.dataframe(df)
            st.button('hi')
        else:
            st.sidebar.write('Wrong Password!')
    else:
        st.sidebar.write('Please Enter Password!')