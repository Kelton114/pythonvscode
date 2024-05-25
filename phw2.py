#Similar Question: University Scholarship Eligibility
#Write a Python program for students to check their scholarship eligibility. Create a menu for the "Check Scholarship" page and the "Scholarship Database" page.

#Ask for the student's name.
#Ask for 5 subjects GPA.
#Based on their average GPA, determine what type of scholarship they are eligible for:
#If their GPA is below 2.5, they are not eligible for a scholarship.
#If their GPA is between 2.5-3.0, they are eligible for a partial scholarship.
#If their GPA is between 3.0-3.5, they are eligible for a half scholarship.
#If their GPA is between 3.5-4.0, they are eligible for a full scholarship.
#Implement the program so that it displays the appropriate message to the student based on their GPA
import streamlit as st
import pandas as pd
import plotly_express as px
st.set_page_config(layout='wide')
df = pd.read_csv('phw2.csv')
menu = st.sidebar.selectbox('Menu',['Check Scholarship','Scholarship Database'])

if menu == 'Check Scholarship':
    st.header('Check Scholarship')
    one, two = st.columns(2)
    with one:
        Name = st.text_input('Enter Name :')
        Science = st.number_input('Please Enter Your Scinece GPA :',0,4)
        ICT = st.number_input('Please Enter Your ICT GPA :',0,4)
    with two:
        Chinese = st.number_input('Please Enter Your Chinese GPA :',0,4)
        English = st.number_input('Please Enter Your English GPA :',0,4)
        Math = st.number_input('Please Enter Your Math GPA :',0,4)
    submit = st.button('Submit')
    if submit:
        if Science:
            if ICT:
                if Chinese:
                    if English:
                        if Math:
                            All = Science + Math + Chinese + ICT + English
                            Average = All/5
                            if Average < 2.5:
                                no_scholarship = 1
                                partial_scholarship = None
                                half_scholarship = None
                                full_scholarship = None
                                student_database = pd.DataFrame({'Name':[Name],'Chinese GPA':[Chinese],'English GPA':[English],'Math GPA':[Math],'Science GPA':[Science],'ICT GPA':[ICT],'Average GPA':[Average],'No Scholarship':[no_scholarship],'Partial Scholarship':[partial_scholarship],'Half Scholarship':[half_scholarship],'Full Scholarship':[full_scholarship]})
                                new_df = pd.concat([df,student_database],ignore_index=True)
                                new_df.to_csv('phw2.csv',index=False)
                                st.success('You Cant Have Any Scolarship')
                            if Average >=2.5 and Average < 3.0:
                                no_scholarship = None
                                partial_scholarship = 1
                                half_scholarship = None
                                full_scholarship = None
                                student_database = pd.DataFrame({'Name':[Name],'Chinese GPA':[Chinese],'English GPA':[English],'Math GPA':[Math],'Science GPA':[Science],'ICT GPA':[ICT],'Average GPA':[Average],'No Scholarship':[no_scholarship],'Partial Scholarship':[partial_scholarship],'Half Scholarship':[half_scholarship],'Full Scholarship':[full_scholarship]})
                                new_df = pd.concat([df,student_database],ignore_index=True)
                                new_df.to_csv('phw2.csv',index=False)
                                st.success('You Can Have Partial Scolarship')
                            if Average >= 3.0 and Average <3.5:
                                no_scholarship = None
                                partial_scholarship = None
                                half_scholarship = 1
                                full_scholarship = None
                                student_database = pd.DataFrame({'Name':[Name],'Chinese GPA':[Chinese],'English GPA':[English],'Math GPA':[Math],'Science GPA':[Science],'ICT GPA':[ICT],'Average GPA':[Average],'No Scholarship':[no_scholarship],'Partial Scholarship':[partial_scholarship],'Half Scholarship':[half_scholarship],'Full Scholarship':[full_scholarship]})
                                new_df = pd.concat([df,student_database],ignore_index=True)
                                new_df.to_csv('phw2.csv',index=False)
                                st.success('You Can Have Half Scolarship')
                            if Average >= 3.5 and Average <=4.0:
                                no_scholarship = None
                                partial_scholarship = None
                                half_scholarship = None
                                full_scholarship = 1
                                student_database = pd.DataFrame({'Name':[Name],'Chinese GPA':[Chinese],'English GPA':[English],'Math GPA':[Math],'Science GPA':[Science],'ICT GPA':[ICT],'Average GPA':[Average],'No Scholarship':[no_scholarship],'Partial Scholarship':[partial_scholarship],'Half Scholarship':[half_scholarship],'Full Scholarship':[full_scholarship]})
                                new_df = pd.concat([df,student_database],ignore_index=True)
                                new_df.to_csv('phw2.csv',index=False)
                                st.success('You Can Have Full Scolarship')
                        else:
                            st.warning('Please Make Sure You Entered All GPA')
                    else:
                        st.warning('Please Make Sure You Entered All GPA')
                else:
                    st.warning('Please Make Sure You Entered All GPA')
            else:
                st.warning('Please Make Sure You Entered All GPA')
        else:
            st.warning('Please Make Sure You Entered All GPA')                            
if menu == 'Scholarship Database':
    st.dataframe(df,use_container_width=True)
    GPA = ['Partial Scholarship','Half Scholarship','Full Scholarship','No Scholarship']
    GPA_ave = df[GPA].count().reset_index()
    GPA_rename = GPA_ave.rename(columns = {'index': 'Subject', 0: 'Average'})
    GPA_rename['Average'] = GPA_rename['Average'].astype(float).round(2).astype(str)
    piechart = px.pie(GPA_rename, names = 'Subject',values='Average')
    st.plotly_chart(piechart)