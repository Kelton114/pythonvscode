import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('barchart.csv')
st.table(df)

Subjects = ['Python','Sql','ML','Tableau','Excel']
Average = df[Subjects].mean().reset_index()
Average_Rename = Average.rename(columns = {'index': 'Subject',0: 'Average'})
Average_Rename['Average'] = Average_Rename['Average'].astype(float).round(2).astype(str) 
st.table(Average_Rename)

barchart = px.bar(Average_Rename,x = 'Subject',y = 'Average')
st.plotly_chart(barchart)