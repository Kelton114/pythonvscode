import streamlit as st
import pandas as pd
df = pd.read_csv('reminder.csv')
st.set_page_config(layout='wide')
Menu = st.sidebar.selectbox('Menu',['Add events','Reminders'])


if Menu == 'Add events':
    select_date = st.date_input('Event date')
    time = st.text_input('Event Time')
    Event_Name = st.text_input('Input Event Name')
    Event_details = st.text_input('Input Event Details')
    Save = st.button('Save')
    if Save:
        Db = {'Date':[select_date],'Time':[time],'Name':[Event_Name],'Details':[Event_details]}
        db = pd.DataFrame(Db)
        new_df = pd.concat([df,db],ignore_index=True)
        new_df.to_csv('reminder.csv',index=False)
        st.success('Data Added')

if Menu == 'Reminders':
    st.subheader('Reminders:')
    date = st.date_input('hi',label_visibility='hidden')

