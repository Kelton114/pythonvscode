#classwork: create a simple app that asks users to enter a number then you can add 10 to their number
import streamlit as st
#num = st.number_input('Input',0)
st.write(st.session_state)



number = st.number_input('Input a number',key='number')
if 'number' not in st.session_state:
    st.session_state.number = 0

    
if st.button('add 10'):
    st.session_state.number += 10
    st.write(st.session_state.number)