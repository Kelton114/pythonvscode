import streamlit as st
import pandas as pd
import plotly_express as px
st.set_page_config(layout='wide')


upload1, upload2 = st.columns(2)

with upload1:
    uploadcsv = st.file_uploader("Upload CSV file",type=['csv'])

if uploadcsv:
    csvfile = pd.read_csv(f'{uploadcsv.name}')
    editfile = st.data_editor(csvfile,use_container_width=True)
    Subjects = csvfile.columns.tolist()
    col1, col2 = st.columns(2)
    with col1:
        ChooseSubject = st.multiselect('Choose your subjects',Subjects)
    with col2:
        chartChoose = st.radio('Choose Chart Type',['Pie','Bar'],horizontal=True)
    SubjectAverage = csvfile[ChooseSubject].mean().reset_index()
    SubjectRename = SubjectAverage.rename(columns= {'index':'Subjects', 0:'Average'})
    pie = px.pie(SubjectRename, names='Subjects', values='Average')
    bar = px.bar(SubjectRename, x = 'Subjects',y = 'Average')
    if chartChoose == 'Pie':
        st.plotly_chart(pie)
    elif chartChoose == 'Bar':
        st.plotly_chart(bar)

    