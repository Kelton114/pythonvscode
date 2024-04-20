"""
-Add a restaurant picture
-Create a restaurant app that welcomes users and shows them the food selections
-If they choose/select their meals, show them the total amount
-Ask a question if you want to share the bill with others #use checkbox
-if yes, then ask how many people want to share the bill #use slider
-Then show the amount each person must contribute to pay the bill
"""
import streamlit as st
bill = 0
st.title("Pay N eat restaurant")
st.image("https://images.pexels.com/photos/708587/pexels-photo-708587.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1")
meal1,meal2,meal3,meal4 = st.columns(4)
with meal1:
    if st.checkbox("Spaghetti & Sauce: $4"):
        if st.checkbox("Red Sauce"):
            st.success("Added to menu")
        if st.checkbox("Black Sauce"):
            st.success("Added to menu")
        bill +=4
with meal2:
    if st.checkbox("Burger $20"):
        if st.checkbox("Original"):
            st.success("Added to menu")
        if st.checkbox("DIY"):
            st.checkbox("Bread")
            st.checkbox("Cheese")
            st.checkbox("Tomato")
            st.checkbox("Onion")
            if st.checkbox("Meat"):
                st.checkbox("1")
                st.checkbox("2")
            st.checkbox("Mushrooms")
            if st.button("Comform"):
                st.success("Added to menu")
        bill +=20
with meal3:
    if st.checkbox("Pizza"):
        if st.checkbox("Tomato Sauce"):
            if st.checkbox("Hawayi Pizza"):
                st.success("Added to menu")
            if st.checkbox("Cheese tomato Pizza"):
                st.success("Added to menu")
        if st.checkbox("Thousand Island Sauce"):
            if st.checkbox("Seafood Pizza"):
                st.success("Added to menu")
            if st.checkbox("Thousand island sauce with smoked salmen pizza"):
                st.success("Added to menu")
        bill +=50
with meal4:
    if st.checkbox("Special golden spaghetti burger Pizza"):
        bill += 100
        st.success("Added to menu")
        st.write("Thankyou for buying this")

if st.button("Total"):
    st.subheader(f"You need to pay {bill} dollars") #f-string helps you put all your statement in one text

if st.checkbox("Click to share your bill with others"):
    people = st.slider("How many people in total?",2,100)
    person = bill / people
    st.subheader(f"The total amount of each people's paymount is {person} dallors")