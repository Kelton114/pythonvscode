
#Project Objective
# Create a student scores database which can
# -get the name done
# -4 subjects done
# -calculate the average
# -calculate the grade (A,B,C,D,E,F)
# -update your csv file


#what is csv file?
#csv file are text files that each data is separated by a comma (comma separated values)


import streamlit as st
import plotly.express as px

import pandas as pd #this is used to read csv files and convert to a table (dataframe)
st.set_page_config(layout='wide')    
df=pd.read_csv('Studentdb.csv', dtype={'Average':str}) #pandas should read this csv file
menu = st.sidebar.selectbox('Menu',['Input Scores','Student Database','Student Chart'])


if menu == 'Input Scores':
    N,E = st.columns(2)
    with N:
        n = st.text_input("Name:")
        m = st.number_input("Math Score",0,100)
        c = st.number_input("Computer Score",0,100)
    with E:
        e = st.number_input("English Score",0,100)
        s = st.number_input("Science Score",0,100)


    st.write(" ")
    st.write(" ")
    submit = st.button("Submit")

    total = e+m+s+c 
    average = total/4
    if average <=100 and average >85:
        grade = ("A")
    if average <=90 and average >80:
        grade = ("B")
    if average <=80 and average >70:
        grade = ("C")
    if average <=70 and average >60:
        grade = ("D")
    if average <=60 and average >50:
        grade = ("E")
    if average <=50:
        grade = ("Fail")
    if submit:
        student_df = pd.DataFrame({'Name':[n],'English':[e],'Maths':[m],'Science':[s],'Computer':[c],'Total':[total],'Average':[average],'Grade':[grade]})
        new_df = pd.concat([df,student_df],ignore_index=True)
        new_df.to_csv('Studentdb.csv',index=False)
        st.success(f'Your total is {total} mark, average is {average} mark, your grade is {grade}')


if menu == 'Student Chart':
    st.title('Students Chart')
    #st.table(df) #streamlit should display as dataframe

    subjects = ['English','Maths','Science','Computer']
    subject_ave = df[subjects].mean().reset_index()
    subjects_rename = subject_ave.rename(columns = {'index': 'Subject', 0: 'Average'})
    subjects_rename['Average'] = subjects_rename['Average'].astype(float).round(2).astype(str)
    #st.table(subjects_rename)

    barchart = px.bar(subjects_rename, x = 'Subject', y = 'Average')

   
    piechart = px.pie(subjects_rename, names = 'Subject',values='Average')
   
    chart_choose = st.radio('Choose Chart',['Pie Chart','Bar Chart'],horizontal=True)
    if chart_choose == 'Pie Chart':
        st.plotly_chart(piechart)
    if chart_choose == 'Bar Chart':
        st.plotly_chart(barchart)
if menu == 'Student Database':
    st.dataframe(df,use_container_width=True)
    with open('Studentdb.csv', 'rb') as file:
        data = file.read()
    st.download_button(label='Download',data=data,file_name='Studentdb.csv')

