import streamlit as st
import pandas as pd
import plotly_express as px
st.set_page_config(layout='centered')
df=pd.read_csv('Chartt.csv')

menu = st.sidebar.selectbox('Menu',['Input Data','Chart'])

if menu == 'Input Data':
    st.title(':blue[Input Player Data]')
    goal = st.radio('Goals Scored',['<10','>=10 and <15','>=15 and <20','>=20'],horizontal=True)
    assists = st.radio('Assists',['<10','>=10 and <15','>=15 and <20','>=20'],horizontal=True)
    tackles = st.radio('Tackles',['<15','>=15 and <25','>=25 and <35','>=35'],horizontal=True)
    passes = st.radio('Passes',['<15','>=15 and <25','>=25 and <35','>=35'],horizontal=True)
    if st.button(':blue[Submit Data]'):
        data = pd.DataFrame({'goal':[goal],'assists':[assists],'tackles':[tackles],'passes':[passes]})
        New_DF = pd.concat([df,data],ignore_index=True)
        New_DF.to_csv('Chartt.csv',index=False)
        st.success('Data Submitted')
if menu == 'Chart':
    st.title(':blue[Chart]')
    st.dataframe(df)
    chatradio = st.radio('Topic',['Goals','Assists','Tackles','Passes'])
    if chatradio == 'Goals':
        Goals = df['goal'].value_counts().reset_index()
        st.dataframe(Goals)
        #Goalsrename = Goals.rename(columns = {'goal': 'Goal','count': 'Count'})
        gbarchart = px.bar(Goals, x='goal',y='count')