import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv('SchoolApp.csv')
CountryLink = pd.read_csv('countries.csv')

menu = st.sidebar.selectbox('Menu',['Application','Data'])
if menu == 'Application':
    st.title('Private School Application Form')
    one, two = st.columns(2)
    with one:
        FirstName = st.text_input('Parent/guardian name:',placeholder='First')
        Age = st.number_input('How old is your child:',0)
    three, four = st.columns(2)
    with two:
        LastName  = st.text_input('Last',placeholder='Last',label_visibility='hidden')
        Gender = st.radio('Child Gender',['Male','Female'],horizontal=True)
    with three:
        ChildFirstName = st.text_input('Child name:',placeholder='First')
    with four:
        ChildLastName = st.text_input('LastName',label_visibility='hidden',placeholder='Last')
    School = st.text_input('The school he comes from:')
    Address = st.text_input('Home address:',placeholder='Street Address')
    Line2 = st.text_input('Street Address Line 2',placeholder='Street Address Line 2',label_visibility='collapsed')
    five, six = st.columns(2)
    with five:
        City = st.text_input('City',label_visibility='collapsed',placeholder='City')
        Postal = st.text_input('Postal/ Zip Code',placeholder='Postal/ Zip Code',label_visibility='collapsed')
    with six:
        Region = st.text_input('Region',placeholder='Region',label_visibility='collapsed')
        Country = st.selectbox('Countries',CountryLink['Country'].tolist(),label_visibility='collapsed')
    number = st.text_input('Phone number:',placeholder='### ### ####')
    Submit = st.button('Submit')
    if Submit:
        dict = {'Parent First Name':[FirstName],'Parent Last Name':[LastName],'Child Age':[Age],'Child Gender':[Gender],'Child First Name':[ChildFirstName],'Child Last Name':[ChildLastName],
                'Origin School':[School],'Street Address':[Address],'Street Address line 2':[Line2],'City':[City],'Region':[Region],'Zip code':[Postal],'Country':[Country],
                'Phone number':[number]}
        dictdf = pd.DataFrame(dict)
        new_dict = pd.concat([df,dictdf],ignore_index=True)
        new_dict.to_csv('SchoolApp.csv',index=False) 
        st.success('Data Added')
if menu == 'Data':

    password = '123'
    passwordInput = st.sidebar.text_input('Please input password',type='password')
    Login = st.sidebar.button('Login')
    st.sidebar.write('Password : 123 to test')
    if Login:
        if passwordInput:
            if passwordInput == password:
                st.dataframe(df,use_container_width=True)
            else:
                st.sidebar.warning('Wrong Password')
        else:
            st.sidebar.warning('Please Enter Password')