#create a simple church age range database
#This will get the name, age, gender of the church memeber
#save this in a database and display on a new page (this page MUST have a login feature)
#Group members in differnt category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )

import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')

menu = st.sidebar.selectbox('Page',['Register','Dataframe'])
if menu == 'Register':
    Name = st.text_input('Please Enter Your Name:')
    age = st.number_input('Please Enter your Age:',0)
    Gender = st.radio('Gender',['Male','Female'])

if age <2 and age >13:
    agerange = ('Kids')
elif age <12 and age >20:
    agerange = ('Teens')
elif age <19 and age >36:
    agerange = ('Youth')
elif age <35 and age >65:
    agerange = ('Adult')
elif age <64:
    agerange = ('Elders')
df = pd.read_csv('church.csv')
if st.button('Submit Data'):
    datadict = ({'Name':[Name],'Age':[age],'Age Range':[agerange],'Gender':[Gender]})
    dataframe = pd.DataFrame(datadict)
    new_df = pd.concat([df,dataframe],ignore_index=True)
    new_df.to_csv('church.csv',index=False)
    st.success('Added Data')




adminpassword = ('12345')
pass1, pass2 = st.sidebar.columns(2)
with pass1:
    password = st.text_input('Please Enter Admin Password')
    loginbutton = st.button('Login')
if loginbutton:
    if password:
        if password == adminpassword:
            df = pd.read_csv('church.csv')
            st.dataframe(df,use_container_width=True)
        else:
            st.sidebar.write('Wrong Password')
    else:
        st.sidebar.write('Please Type Password')