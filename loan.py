import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
df=pd.read_csv('loan.csv')
User_id = 'User' + str(len(df) + 1)
menu = st.sidebar.selectbox('Employee',['Register Here','Loan data base','Find User'])
if menu == ('Register Here'):
    st.header('Loan Application Form')
    st.text('Please fill the imformation below')
    st.write('')
    text, braket = st.columns(2)
    with text:
        st.subheader('Desired loan amount')
        st.subheader('Annual Income')
        st.subheader('Reanson for loan?')
        st.subheader('Your name')
        st.subheader('Birth date')
        st.subheader('Phone number')
        st.subheader('Email')
        st.subheader('Adress')
    with braket:
       LoanAmount = st.text_input('Usd1',placeholder='USD 0',label_visibility='collapsed')
       AnnualIncome = st.text_input('Usd2',placeholder='USD 0',label_visibility='collapsed')
       UseForLoan = st.selectbox('choose',['Business','Health','Home','Purchase','Home' ,'Renovation','Education','Traveling','Vacation','Relocation'],label_visibility='collapsed')
       firstname, lastname = st.columns(2)
       with firstname:
           first = st.text_input('First',placeholder='First',label_visibility='collapsed')
       with lastname:
           secound = st.text_input('Last',placeholder='Last',label_visibility='collapsed')
       Birthdate = st.date_input('date',format='DD/MM/YYYY',value=None,label_visibility='collapsed')
       PhoneNumber = st.text_input('pn',placeholder='#### ####',label_visibility='collapsed')
       Email = st.text_input('EEmail',label_visibility='collapsed')
       Adress = st.text_input('Adrees',placeholder='Street Address',label_visibility='collapsed')
    if st.button('Submit'):
        loan_df = pd.DataFrame({'User Id':[User_id],'Firstname':[first],'Lastname':[secound],'Loan Amount':[LoanAmount],'Use of Loan':[UseForLoan],'Annual Income':[AnnualIncome],'Birthdate':[Birthdate],
                                'Phone number':[PhoneNumber],'Email':[Email]})
        new_df = pd.concat([df,loan_df],ignore_index=True)
        new_df.to_csv('loan.csv',index=False)
        st.success('Loan added')

if menu == 'Loan data base':
    st.dataframe(df,use_container_width=True)