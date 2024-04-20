#Create a menu for Registration and Database
#Design a blood donation database that can get donor input
#-Name -Contact Number
#-Blood group(A,AB,AB-,AB+,B,O) -Disease/Infection(Yes/No)

#-Submit donor details

#Next, save these in a csv file and show the database in a Database page in the menu

import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df=pd.read_csv('BloodDonation.csv')

menu = st.sidebar.selectbox('Menu',['Registration','Database'])
if menu == 'Registration':
    st.header('Registration Page')
    a, b = st.columns(2)
    with a:
        Name = st.text_input('What is your Name?')
        BloodGroup = st.selectbox('Blood Group',['A','B','AB+','AB-','O'])
    with b:
        ContactNumber = st.text_input('Plase input your contact number')
        Disease = st.radio('Do you have any disease?',['Yes','No'])
    Submit = st.button('Submit')
    if Submit:
        donation_df = pd.DataFrame({'Name':[Name],'Contact Number':[ContactNumber],'Blood type':[BloodGroup],'Disease':[Disease]})
        new_df = pd.concat([df,donation_df],ignore_index=True)
        new_df.to_csv('BloodDonation.csv',index=False)
        st.success('Submited')
if menu == 'Database':
    st.dataframe(df,use_container_width=True)


