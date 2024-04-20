import streamlit as st
st.title("Welcome")
st.header("How many Ice cream do you want to buy?")
ice = st.number_input("I would like to buy" ,1,value=1)
if st.button("comform"):
    st.write("Thankyou for buying, it would be", 25*ice, "dolars please")