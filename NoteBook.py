import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')
readcsv = pd.read_csv('NoteBook.csv')
menu = st.sidebar.selectbox('Selevt Action',['Create Note','View Note','Update Note'])
if menu == 'Create Note':
    
    st.header(':orange[Create A New Note]')
    c1, c2 = st.columns(2)
    with c1:
        notetitle = st.text_input('Enter the title for your new note')
    with c2:
        notedate = st.date_input('Select Note Date')
    notecontent = st.text_area('Enter your new note',height=200)
    if st.button('Save Note'):
        notedict = {'Title':[notetitle],'Date':[notedate],'Content':[notecontent]}
        notedf = pd.DataFrame(notedict)
        combinednotes = pd.concat([readcsv,notedf],ignore_index=True)
        combinednotes.to_csv('NoteBook.csv',index=False)
        st.success('Note Saved Sucessfully')

if menu == 'View Note':
    st.header(':orange[Select Note To View]')
    notetitles = readcsv['Title'].tolist()
    #st.write(notetitles)
    three,four = st.columns(2)
    with three:
        select_notetitle = st.selectbox('Select a note',notetitles)
    filtertitle = readcsv[readcsv['Title'] == select_notetitle]
    one, two = st.columns(2)
    with one:
        st.subheader(f':blue[{select_notetitle}]')
    date = filtertitle['Date'].iloc[0]
    with two:
        st.subheader(f':green[{date}]')
    st.divider()
    #st.write(filtertitle)
    content = filtertitle['Content'].iloc[0]
    st.write(content)
if menu == 'Update Note':
    st.header(':orange[Select Note To View]')
    notetitles = readcsv['Title'].tolist()
    #st.write(notetitles)
    three, four = st.columns(2)
    select_notetitle = st.selectbox('Select a note',notetitles)
    filtertitle = readcsv[readcsv['Title'] == select_notetitle]
    one, two = st.columns(2)
    with one:
        st.subheader(f':blue[{select_notetitle}]')
    date = filtertitle['Date'].iloc[0]
    with two:
        st.subheader(f':green[{date}]')
    st.divider()
    #st.write(filtertitle)
    content = filtertitle['Content'].iloc[0]

    updatenote = st.text_area('Edit teh selected note',content,height=200 )

    if st.button('Save Updated Note'):
        readcsv.loc[readcsv['Title'] == select_notetitle, 'Content'] = updatenote
        #st.write(content)
        readcsv.to_csv('NoteBook.csv',index=False)
        st.success('Note Update Successfully')