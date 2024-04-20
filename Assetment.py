#CLASS ASSESSMENT
#1.What is streamlit used for?
#2.show 8 ways to display text on streamlit
#3.show how to ask for a text on streamlit 
#4.show how to ask for a number on streamlit
#5.create a button on the left column but show the output on the right column
#6.create a radio button with a horizontal orientation
#7.import an image with a 150*150 size
#8. read and dispay a CSV file in python
#9.create a toggle option to display any database/dataframe
#10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file)
#and convert it to a dataframe/table

#1.Streamlit is used for that user can interect with program
#2.st.write('hi'), st.success('hi'),st.warning('hi'),st.header('hi'),st.subheader('hi'),st.text_input('hi'),st.number_input('hi'),st.date_input('hi')
#3.st.text_input('hi')
#4.st.number_input('hi')
#5.
        #one, two = st.columns(2)
        #with one:
            #hi = st.button('click')
        #with two:
            #if hi:
                #st.warning('hi')
#6.
        #hi = st.radio('hi',['hi','hi2'],horizontal=True)
#7.
        #st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/1392f2e3-d214-440d-8a97-65e1d6f5a460/dcthe25-c3f48252-f92b-4e35-8462-ca3caaa4b09a.png/v1/fill/w_150,h_150/_f2u__woods__by_raridecor_dcthe25-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTUwIiwicGF0aCI6IlwvZlwvMTM5MmYyZTMtZDIxNC00NDBkLThhOTctNjVlMWQ2ZjVhNDYwXC9kY3RoZTI1LWMzZjQ4MjUyLWY5MmItNGUzNS04NDYyLWNhM2NhYWE0YjA5YS5wbmciLCJ3aWR0aCI6Ijw9MTUwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.g4i7eTcNkKxKLk7zljaoSIpZ9BNWkZ1myTPsKV6yWuw')
#8.
        #df = pd.read_csv('Assetment.csv')
        #st.dataframe(df,use_container_width=True)
#9.     #if st.button('hi'):
            #df = pd.read_csv('Assetment.csv')
            #st.dataframe(df,use_container_width=True)
#10.
import streamlit as st
import pandas as pd
Car = st.text_input('Input Car Name')
Brand = st.text_input('Input Car Brand')
Speed = st.number_input('Input Car Speed',0)
Color = st.color_picker('Input Car Color')
Price = st.number_input('Input Car Price',0)
if st.button('Submit'):
    Cardict = {'Car':Car,'Brand':Brand,'Speed':Speed,'Color':Color,'Price':Price}
    st.dataframe(Cardict)
