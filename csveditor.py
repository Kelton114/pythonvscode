import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')


upload1, upload2 = st.columns(2)

with upload1:
    uploadcsv = st.file_uploader("Upload CSV file",type=['csv'])

if uploadcsv:
    csvfile = pd.read_csv(uploadcsv)
    editfile = st.data_editor(csvfile,use_container_width=True)

    save1,save2 = st.columns(2)
    with save1:
        if st.button('Save on Original File'):
            savedfile = editfile.to_csv(uploadcsv.name,index=False)
            st.success('Edited CSV File Saved')

    with save2:
        with open(uploadcsv.name,'rb') as file: #open to make the file readable as each character
            data = file.read() #read the content
        st.download_button(label='Download Edited CSV file',data=data,file_name=uploadcsv.name)