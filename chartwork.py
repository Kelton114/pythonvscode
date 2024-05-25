#-read the CSV file and display in as a  table (data frame) 

#-plot a bar chart of countries against sales 

#-plot a pie chart of product category section against the sales 

#-repeat plots in step 1 and 2 charts against profit

import streamlit as st
import pandas as pd
import plotly_express as px
st.set_page_config(layout='wide')
df = pd.read_csv("Chartwork.csv")
menu = st.sidebar.selectbox('Menu',['Data Base','Charts'])
if menu == 'Data Base':
    st.header('Data Base')
    st.dataframe(df,use_container_width=True,height=750)

if menu == 'Charts':
    st.title('Chart')


    sales = df[['Sales','City','Category']].reset_index()
    sales_rename = sales.rename(columns = {'index': 'City', 0: 'Sales'})
 

    barchart = px.bar(sales, x = 'City', y = 'Sales')




    piechart = px.pie(sales_rename, names = 'Category',values='Sales')
   
    chart_choose = st.radio('Choose Chart',['Pie Chart','Bar Chart'],horizontal=True)
    if chart_choose == 'Pie Chart':
        st.plotly_chart(piechart)
    if chart_choose == 'Bar Chart':
        st.plotly_chart(barchart)

