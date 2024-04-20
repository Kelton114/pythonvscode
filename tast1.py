#TEST 1
#write a python program for house buyers
#Ask them for their name
#ask them for their yearly salary
#If the earn between 100000-500,000 they can buy a bungalow
#If the earn between >500,000-1,000,000 they can buy a duplex
#If the earn between >1,000,000-5,000,000 they can buy a manshion
#create a database to to store and view their answers and display in another customer section

import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('tast1.csv')
st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('Menu',['Registration','Database'])
if menu == 'Registration':
    st.header('Registration')
    one, two = st.columns(2)
    with one:
        Name = st.text_input('Name')
    with two:
        Salary = st.number_input('Yearly Salary',0)
    Submit = st.button('Submit')

    if Submit:
        if Salary >= 100000 and Salary <= 500000:
             Bungalow = 'Yes'
             Duplex = None
             Manshion = None
             st.write('You can purchase a Bungalow')
        elif Salary >500000 and Salary <=1000000:
             Bungalow = 'Yes'
             Duplex = 'Yes'
             Manshion = None
             st.write('You can purchase a Bungalow and a Duplex')
        elif Salary >1000000:
             Bungalow = 'Yes'
             Duplex = 'Yes'
             Manshion = 'Yes'
             st.write('You can purchase a Bungalow, a Duplex and a Mansion')
        elif Salary <100000:
             st.write('You can not buy anything')
             Bungalow = None
             Duplex = None
             Manshion = None
        data = pd.DataFrame({'Name':[Name],'Yearly Salary':[Salary],'Bungalow':[Bungalow],'Duplex':[Duplex],'Manshion':[Manshion]})
        new_data = pd.concat([df,data],ignore_index=True)
        new_data.to_csv('tast1.csv',index=False)
        st.success('Submit Successful')
        
if menu == 'Database':
        st.table(df)
     

