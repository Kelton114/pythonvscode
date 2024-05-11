import streamlit as st
import pandas as pd
from fpdf import FPDF
st.set_page_config(layout='wide')
df=pd.read_csv('employeedb.csv')
employee_id = 'User' + str(len(df) + 1)
menu = st.sidebar.selectbox('Employee',['Register Here','Employee data base','Employee File'])
if menu == 'Register Here':
    st.header('Register Here')
    firstn, lastn = st.columns(2)
    with firstn:
        firstname = st.text_input('Enter your firstname')
        email = st.text_input('Enter your email')
        el = st.selectbox("Education level",["Masters","Bacherlors","OND","HND"])
        department = st.selectbox('Department',['Security','Cleaning','IT','Sales','Finance','Purchasing','Accounting','Operations','Marketing','Researsh and development','Production','General management','Administration'])
        date = st.date_input('Enter the Employment date')
    with lastn:
        lastname = st.text_input('Enter your lastname')
        gender=st.radio("Gender",["Male","Female"],horizontal=True)
        salary = st.number_input('Enter your monthly salary',0)
        jobtitle = st.selectbox('Job title',['Entry','Individual Contributor','Manager','Director','Vice chief','Chief','Chairperson'])
        employeestatus = st.selectbox('Employee status',['Part time','Full time'])
    Registration = st.date_input('Enter the Registration date')
    if st.button('Add Employee Data'):
        employee_df = pd.DataFrame({'User ID':[employee_id],'First Name':[firstname],'Last Name':[lastname],'Email Address': [email],'Gender':[gender],'Education Level':[el],
                    'Salary':salary,'Department':[department],'Job Title':[jobtitle],'Employment Date':[date],'Employee Status':[employeestatus],'Registration Date':[Registration]})
        new_df = pd.concat([df,employee_df],ignore_index=True)
        new_df.to_csv('employeedb.csv',index=False)
        st.success('New Employee Added')
if menu == 'Employee File':
    s1,s2,s3 = st.columns(3)
    with s3:
        st.header('Find Employee Details')
        EmployeeID = st.text_input('Search Employee Details')
        Search = st.button('Find Employee')
    if Search:
            if EmployeeID:
                search_result = df[df['User ID'].str.lower() == EmployeeID.lower()]
                if not search_result.empty:
                    getfn = search_result['First Name'].iloc[0]
                    getln = search_result['Last Name'].iloc[0]
                    getEmail = search_result['Email Address'].iloc[0]
                    getGender = search_result['Gender'].iloc[0]
                    getel = search_result['Education Level'].iloc[0]
                    getsa = search_result['Salary'].iloc[0]
                    getde = search_result['Department'].iloc[0]
                    getjt = search_result['Job Title'].iloc[0]
                    geted = search_result['Employment Date'].iloc[0]
                    getes = search_result['Employee Status'].iloc[0]
                    getrd = search_result['Registration Date'].iloc[0]
                    getid = search_result['User ID'].iloc[0]
                    st.success('Employee found')
                    st.header(f':orange[{getfn} {getln}]')
                    st.header('')
                    st.header('Personal Information')
                    st.divider()
                    a, b, c = st.columns(3)
                    with a:
                        st.write('Email')
                        st.write(getEmail)
                    with b:
                        st.write('Gender')
                        st.write(getGender)
                    with c:
                        st.write('Education Level')
                        st.write(getel)
                    st.divider()
                    e, f, g = st.columns(3)
                    with e:
                        st.write('Department')
                        st.write(getde)
                    with f:
                        st.write('Employee ID')
                        st.write(getid)
                    with g:
                        st.write('Date Of Employment')
                        st.write(geted)
                    st.divider()
                    h, i, j = st.columns(3)
                    with h:
                        st.write('Job Title')
                        st.write(getjt)
                    with i:
                        st.write('Employee Status')
                        st.write(getes)
                    with j:
                        st.write('Salary')
                        st.write(f'**${getsa:,}**')
                    if st.sidebar.button('Download Use FIle'):
                        def design_pdf():
                            pdf = FPDF() #keyword to activate, name your pdf variable
                            pdf.add_page() #keyword to create new page

                            pdf.set_font('Arial', size=12)
                            pdf.set_xy(20,20)
                            pdf.cell(40,text=f':orange[{getfn} {getln}]',ln=True,align='L')
                    if st.sidebar.button('View'):
                        pass
                else:
                    st.error('User not found')  


if menu ==('Employee data base'):
    st.dataframe(df,use_container_width=True)






