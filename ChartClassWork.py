import streamlit as st
import pandas as pd
import plotly_express as px

#EXAM 100 MARKS

#EXAM 100 MARKS

#-CREATE A NEW FILE AND ASK THE COACH TO SUBMIT THE STUDENTS 
#NAME OF PLAYER
#GOALS SCORED
#ASSIST MADE
#TACKLES MADE


#-SAVE IN A CSV FILE - 20 MARKS

#-SHOW THE DICTIONARY OF THE RESPONSE -20 MARKS

#-SHOW THE TABLE OF THE RESPONSE - 5MARKS

#-SHOW THE TABLE FROM THE CSV FILE AT THE TOP (ABOUT 10 SAVED RESPONSES)
#10 MARKS

#-PLOT A BARCHART OF THE NAMES AGAINST THE GOALS SCORED -20 MARKS

#-PUT A COMMENT IN EVERY LINE TO EXPLAIN WHAT THE CODE DOES -5 MARKS
df = pd.read_csv('ChartClassWork.csv')
menu = st.sidebar.selectbox('Menu',['Input Studebt Data','View Student Data'])  #Make Menu
if menu == 'Input Studebt Data':  #Condition
    st.header('Input Player Data') # Place Header
    
    Name = st.text_input('Please Enter Name Of Player:') #Ask for Name
    Goal = st.number_input('Goal Number',0)  #Ask For Goal NUmber
    Assist = st.number_input('Assist Number',0)  #Ask For Assist Number
    Tackle = st.number_input('Tackle Number',0)  #Ask For Tackle Number)
    Save = st.button('Save') #Button
    if Save: #Condition
        Data = pd.DataFrame({'Name':[Name],'Goal':[Goal],'Assist':[Assist],'Tackle':[Tackle]}) #Make DataFrame From Dictionary
        New_Data = pd.concat([df,Data],ignore_index=True)#Concat Data Frame
        New_Data.to_csv('ChartClassWork.csv',index=False)#Send To Csv File
        st.success('Player Data Added') #Success
if menu == 'View Student Data':#Condition
    st.header('View Student Data')#Header
    st.dataframe(df,use_container_width=True)
    #Goals = df['Goal','Name']
    #st.dataframe(Goals)
    chart_radio = st.radio('Choose Chart',['Goals','Tackles','Assists'],horizontal=True)
    if chart_radio == 'Goals':
        GoalChart = px.bar(df, x='Name',y='Goal')
        st.plotly_chart(GoalChart)
    if chart_radio == 'Tackles':
        TacklesChart = px.bar(df,x='Name',y='Tackle')
        st.plotly_chart(TacklesChart)
    if chart_radio == 'Assists':
        AssistChart = px.bar(df,x='Name',y='Assist')
        st.plotly_chart(AssistChart)