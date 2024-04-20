import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
Car, Color, Brand, Price, Speed, Weight = st.columns(6)
with Car:
    fCar = st.text_input('Input 1st car name')
    sCar = st.text_input('Input 2nd car name')
    tCar = st.text_input('Input 3rd car name')
    foCar = st.text_input('Input 4th car name')
    fiCar = st.text_input('Input 5th car name')
with Color:
    fColor = st.color_picker('Input 1st car color')
    st.write('')
    sColor = st.color_picker('Input 2nd car color')
    st.write('')
    tColor = st.color_picker('Input 3rd car color')
    st.write('')
    foColor = st.color_picker('Input 4th car color')
    st.write('')
    fiColor = st.color_picker('Input 5th car color')
with Brand:
    fBrand = st.text_input('Please Input 1st Car Brand')
    sBrand = st.text_input('Please Input 2nd Car Brand')
    tBrand = st.text_input('Please Input 3rd Car Brand')
    foBrand = st.text_input('Please Input 4th Car Brand')
    fiBrand = st.text_input('Please Input 5th Car Brand')  
with Price:
    fPrice = st.number_input('Please Input 1st Car Price',0)
    sPrice = st.number_input('Please Input 2nd Car Price',0)
    tPrice = st.number_input('Please Input 3rd Car Price',0)
    foPrice = st.number_input('Please Input 4th Car Price',0)
    fiPrice = st.number_input('Please Input 5th Car Price',0)
with Speed:
    fSpeed = st.number_input('Please Input 1st Car speed',0)
    sSpeed = st.number_input('Please Input 2nd Car speed',0)
    tSpeed = st.number_input('Please Input 3rd Car speed',0)
    foSpeed = st.number_input('Please Input 4th Car speed',0)
    fiSpeed = st.number_input('Please Input 5th Car speed',0)
with Weight:
    fWeight = st.number_input('Please Input 1st Car Weight',0)
    sWeight = st.number_input('Please Input 2nd Car Weight',0)
    tWeight = st.number_input('Please Input 3rd Car Weight',0)
    foWeight = st.number_input('Please Input 4th Car Weight',0)
    fiWeight = st.number_input('Please Input 5th Car Weight',0)