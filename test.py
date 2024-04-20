import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
df=pd.read_csv('test.csv')


Age = st.number_input('Age:',0)
Name = st.text_input('Name:')
Height = st.number_input('Height:',0)
submit = st.button('Submit')
if submit:
    persondict = {'Name':[Name],'Age':[Age],'Height':[Height]}
    person = pd.DataFrame(persondict)
    newperson = pd.concat([df,person],ignore_index=True)
    newperson.to_csv('test.csv',index=False)
    st.success('Submited')

st.dataframe(df,use_container_width=True)