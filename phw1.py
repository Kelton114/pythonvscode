#Write a Python program for car buyers. Create a menu for the "Buy Car" page and the "Car Database" page.


#Ask for the buyer's name.
#Ask for their yearly salary.
#Based on their yearly salary, determine what type of car they can afford:
#If they earn below $30,000, they can buy a used car.
#If they earn between $30,000-$60,000, they can buy an economy car.
#If they earn between $60,000-$100,000, they can buy a mid-range car.
#If they earn between $100,000-$200,000, they can buy a luxury car.
#If they earn above $200,000, they can buy a supercar.
#Implement the program so that it displays the appropriate message to the buyer based on their salary.

import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
df = pd.read_csv('phw1.csv')
menu = st.sidebar.selectbox('Menu',['Cars','Car Database'])
if menu == 'Cars':
    st.header('What Car Can You afford ?')
    one, two =st.columns(2)
    with one:
        Name = st.text_input('Enter Your Name :')
    with two:
        Salary = st.number_input('Please Enter Your Salary',0)
    Submit = st.button('Submit')
    if Submit :
        if Salary:
            if Salary < 30000:
                
                Used_Car = 1
                Economy_Car = None
                MidRange_Car = None
                Luxury_Car = None
                Super_Car = None
                cars_df = pd.DataFrame({'Name':[Name],'Salary':[Salary],'Used Car':[Used_Car],'Economy Car':[Economy_Car],'Mid Range Car':[MidRange_Car],'Luxury Car':[Luxury_Car],'Super Car':[Super_Car]})
                new_df = pd.concat([df,cars_df],ignore_index=True)
                new_df.to_csv('phw1.csv',index=False)
                st.success('You Can Buy A Used Car')
            elif Salary >= 30000 and Salary < 60000:
                st.success('You Can Buy A Used Car or An Economy Car')
                Used_Car = 1
                Economy_Car = 1
                MidRange_Car = None
                Luxury_Car = None
                Super_Car = None
                cars_df = pd.DataFrame({'Name':[Name],'Salary':[Salary],'Used Car':[Used_Car],'Economy Car':[Economy_Car],'Mid Range Car':[MidRange_Car],'Luxury Car':[Luxury_Car],'Super Car':[Super_Car]})
                new_df = pd.concat([df,cars_df],ignore_index=True)
                new_df.to_csv('phw1.csv',index=False)
            elif Salary >= 60000 and Salary < 100000:
                st.success('You Can Buy A Used Car or An Economy Car or a Mid-range Car')
                Used_Car = 1
                Economy_Car = 1
                MidRange_Car = 1
                Luxury_Car = None
                Super_Car = None
                cars_df = pd.DataFrame({'Name':[Name],'Salary':[Salary],'Used Car':[Used_Car],'Economy Car':[Economy_Car],'Mid Range Car':[MidRange_Car],'Luxury Car':[Luxury_Car],'Super Car':[Super_Car]})
                new_df = pd.concat([df,cars_df],ignore_index=True)
                new_df.to_csv('phw1.csv',index=False)
            elif Salary >= 100000 and Salary <= 200000:
                st.success('You Can Buy A Used Car or An Economy Car or A Mid-range Car or A Luxury Car')
                Used_Car = 1
                Economy_Car = 1
                MidRange_Car = 1
                Luxury_Car = 1
                Super_Car = None
                cars_df = pd.DataFrame({'Name':[Name],'Salary':[Salary],'Used Car':[Used_Car],'Economy Car':[Economy_Car],'Mid Range Car':[MidRange_Car],'Luxury Car':[Luxury_Car],'Super Car':[Super_Car]})
                new_df = pd.concat([df,cars_df],ignore_index=True)
                new_df.to_csv('phw1.csv',index=False)
            elif Salary > 200000:
                st.success('You Can Buy A Used Car or An Economy Car or A Mid-range Car or A Luxury Car or A Super Car')
                Used_Car = 1
                Economy_Car = 1
                MidRange_Car = 1
                Luxury_Car = 1
                Super_Car = 1
                cars_df = pd.DataFrame({'Name':[Name],'Salary':[Salary],'Used Car':[Used_Car],'Economy Car':[Economy_Car],'Mid Range Car':[MidRange_Car],'Luxury Car':[Luxury_Car],'Super Car':[Super_Car]})
                new_df = pd.concat([df,cars_df],ignore_index=True)
                new_df.to_csv('phw1.csv',index=False)
        else:
            st.warning('Please Enter Your Salary')
if menu == 'Car Database':

    st.dataframe(df,use_container_width=True)