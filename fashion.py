"""
FASHION STORE PAGE AND ABOUT US PAGE
A fashion app 
-title
-image
-categories
Men's Fashion

Women's Fashion

Children's Fashion

(each category must havedifferent types of unique items and the prices like shirts(long sleeves,short, round neck, polo etc), boxers, trousers, shoes, bags etc)"""


import streamlit as st

menu = st.sidebar.selectbox('Fashion Menu',['Male Fashion','Female Fashion','Kids Fashion','About Us'])


if menu == 'Male Fashion':
    st.title("Welcome to Kelton Fashion Store")
    st.subheader("Male fashion")
    st.image("https://fashionista.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_760/MTQ4MTI3OTEyOTM4MTg2MjYy/hp-paris-fashion-week-mens-spring-2018-street-style.webp")
    jacket, cloth = st.columns(2)
    Pants, shoes = st.columns(2)
    with jacket:
        if st.checkbox("Jacket"):
            if st.checkbox("Denim Jacket"):
                st.image("https://www.jdinstitute.edu.in/media/2021/07/Jackets-For-Men-5-Types-And-How-To-Style-Them-3.jpg")
                st.color_picker("COLOR",key="1")
            if st.checkbox("Utility Jacket"):
                st.image("https://www.jdinstitute.edu.in/media/2021/07/Jackets-For-Men-5-Types-And-How-To-Style-Them-4.jpg")
                st.color_picker("COLOR",key="2")
    with cloth:
        if st.checkbox("Clothes"):
            if st.checkbox("sweatshirt"):
                st.image("https://static.thcdn.com/images/large/webp//productimg/1600/1600/12374095-4044770454670670.jpg")
                st.color_picker("COLOR",key="3")
                if st.checkbox("Do you want any Text on the sweatshirt?"):
                    st.text_input("Text",key="sweatshirt")
            if st.checkbox("T-shirt"):
                st.image("https://diwu.pl/1033-large_default/tshirt-unisex-oversized.jpg")
                st.color_picker("COLOR",key="4")
                if st.checkbox("Do you want any text on the T shirt?"):
                    st.text_input("Text",key="T-shirt")










if menu == 'About Us':
    st.title("Here is about us")