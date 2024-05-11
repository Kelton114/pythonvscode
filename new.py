#Create a voting application which accepts user input for age. Checks if they are eligible to vote or not. If they are eligible to vote, they can enter their candidiates name and vote(they get a response that says they’ve successfully voted).

#Minimum age for voting is 18.
import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df=pd.read_csv('new.csv')

menu = st.sidebar.selectbox('Menu',['Vote','Data Base'])
if menu == 'Vote':
    st.header('Vote')
    st.write(f':red[You can only vote once you are OVER or EQUAL to 18 years old]')
    age = st.number_input('Please Enter Your Age',0)
    if age:
        if age < 18:
            st.warning('You Can Not Vote Yet')
            ein, swei, drei = st.columns(3)
            with swei:
                st.image(image='https://static.vecteezy.com/system/resources/previews/005/001/661/non_2x/under-18-forbidden-round-icon-sign-illustration-eighteen-or-older-persons-adult-content-18-plus-only-rating-isolated-on-white-background-vector.jpg',width=300)

        if age >=18:
            one, two = st.columns(2)
            with one:
                Fname = st.text_input('Please Type Your First Name')
            with two:
                Lname = st.text_input('Please Type Your Last Name')
            candidiate = st.text_input('Enter Your Candidiate Name')
            submit = st.button('Submit')
            if submit:
                vote_df = pd.DataFrame({'Age':[age],'First Name':[Fname],'Last Name':[Lname],'candidiate': [candidiate]})
                new_df = pd.concat([df,vote_df],ignore_index=True)
                new_df.to_csv('new.csv',index=False)
                st.success('Vote Added')
if menu == 'Data Base':
    st.dataframe(df,use_container_width=True)