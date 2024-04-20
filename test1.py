import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
df=pd.read_csv('test1.csv')
menu = st.sidebar.selectbox('Menu',['student details','database'])
if menu == 'student details':
    namee, ageee = st.columns(2)
    with namee:
        Name = st.text_input('Name:')

    with ageee:
        age = st.number_input('Age:',0)
    submit = st.button('Submit')
    if submit:
        person = pd.DataFrame({'Name':[Name],'Age':[age]})
        newperson = pd.concat([df,person],ignore_index=True)
        newperson.to_csv('test1.csv',index=False)
        st.success('Submited')
if menu == 'database':
    st.dataframe(df,use_container_width=True)