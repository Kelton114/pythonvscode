import streamlit as st
from fpdf import FPDF
import pandas as pd
import base64 #python module to convert binary data (code) to printable character(pdf)
df=pd.read_csv('invoice.csv')
CName = df['Name'].iloc[0]
CCountry = df['Country'].iloc[0]
CBankAccName = df['Bank Account Name'].iloc[0]
CAddress = df['Address'].iloc[0]
CBankName = df['Bank Name'].iloc[0]
CBankNumber = df['Bank Number'].iloc[0]

menu = st.sidebar.selectbox('Menu',['Invoice Generator','Change Details'])
if menu == 'Invoice Generator':
    st.header('Invoice Generator')
    tax = st.sidebar.number_input('Enter Tax %',0.00,100.00)
    Discount = st.sidebar.number_input('Enter Discount %',0.00,100.00)
    cola1, cola2, cola3, cola4 = st.columns(4)
    with cola1:
        st.image('logo-Meta.png',use_column_width=True)
    with cola4:
        st.write('')
        st.header(':blue[INVOICE]')
    colb1,colb2,colb3, = st.columns(3)
    with colb1:
        st.write(f':blue[{CName}]')
        st.write(f':blue[{CAddress}]')
        st.write(f':blue[{CCountry}]')
    colc1,colc2= st.columns(2)
    with colc1:
        name = st.text_input(':blue[Bill to:]',placeholder='Name of Bill Receiver')
        email = st.text_input(':blue[Email Address:]',label_visibility='collapsed',placeholder='Email Address')
    with colc2:
        colc2a,colc2b = st.columns(2)
        with colc2a:
            
            st.write(':blue[Invoice:]')
            st.write('')
            st.write(':blue[Invoice Date:]')
            st.write('')
            st.write(':blue[Due Date:]')
        with colc2b:
            invoice = st.text_input('sdsd',label_visibility='collapsed')
            indate = st.date_input('fgfgf',label_visibility='collapsed')
            day = indate.day
            month = indate.strftime('%B') #Full month: January,%b=short month: Jan
            year = indate.year
            indate = f'{day} {month} {year}'

            duedate = st.date_input('hjhjh',label_visibility="collapsed")
            dday = duedate.day
            dmonth = duedate.strftime('%B')
            dyear = duedate.year
            duedate = f'{dday}  {dmonth} {dyear}'

    st.write('')
    cold1,cold2,cold3,cold4 = st.columns(4)
    with cold1:
        Describtion = st.text_input(':blue[Description]')
    with cold2:
        quantity = st.number_input(':blue[Quantity]',0)
    with cold3:
        PriceUnit = st.number_input(':blue[Price|Unit]',0)
        
    with cold4:
        price = quantity*PriceUnit
        
        taxDivide = price/100
    with cold3:
        taxAmount = st.write(f':blue[Tax : ${taxDivide*tax}]')
    with cold4:
        taxnumber = taxDivide*tax
        Discountnumber = taxDivide*Discount
        OverallPrice = price+taxnumber-Discountnumber
        totalPrice = st.text_input(':blue[Total Price]',value=price,disabled=True)
        DiscountAmount = st.write(f':blue[Discount : ${taxDivide*Discount}]')

    st.write('----------')
    cole1,cole2 = st.columns(2)
    with cole1:
        st.write(':blue[Payment Info]')
        st.write(f':blue[Acc name: {CBankAccName}]')
        st.write(f':blue[Acc Number: {CBankNumber}]')
        st.write(f':blue[Bank Name: {CBankName}]')
        view = st.button(':blue[View inovioce]')
    with cole2:
        st.write(':blue[Payment Due:]')
        st.header(f':green[${OverallPrice:,}]')


    #Generate a pdf

    def generate_pdf():
        pdf = FPDF()

        #Add a page
        pdf.add_page()

        #set your default fonts
        pdf.set_font('Arial',size=12)

        colx = 20
        coly = 20
        colw= 90

        pdf.image('logo-Meta.png',x=colx,y=coly,w=20)
        #FONTS: Courier, Arial, Times, Symbol

        #invoice
        pdf.set_font(family='Times',size=30,style='B')
        pdf.set_xy(colx+110,coly+5)
        pdf.cell(w=colw,txt='INVOICE',ln=True,align='L')

        #Faisa|tech
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+25)
        pdf.cell(w=colw,txt=CName,ln=True,align='L')

        #471, Camelia 7,Arabian Ranches 8
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+35)
        pdf.cell(w=colw,txt=CAddress,ln=True,align='L')

        #Dubai, UAE
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+45)
        pdf.cell(w=colw,txt=CCountry,ln=True,align='L')

        #Bill to
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+70)
        pdf.cell(w=colw,txt='Bill to :',ln=True,align='L')

        #Name
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+80)
        pdf.cell(w=colw,txt=f'{name}',ln=True,align='L')

        

        #Email Addresss
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+90)
        pdf.cell(w=colw,txt=f'{email}',ln=True,align='L')
        
        
        #Invoice:
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+110,coly+80)
        pdf.cell(w=colw,txt=f'Invoice:',ln=True,align='L')

        #Invoice Date:
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+110,coly+90)
        pdf.cell(w=colw,txt=f'Invoice Date:',ln=True,align='L')


        #Draw Line
        pdf.set_line_width(0.5)#width of line
        pdf.line(colx,coly+120,colx+180,coly+120)#start xy and the stop xy
        #in
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+150,coly+80)
        pdf.cell(w=colw,txt=f'{invoice}',ln=True,align='L')

        #in
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+150,coly+90)
        pdf.cell(w=colw,txt=f'{indate}',ln=True,align='L')

        #Describtion
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx+0,coly+115)
        pdf.cell(w=colw,txt=f'DESCRIBTION:',ln=True,align='L')

        #Describtion info
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+0,coly+125)
        pdf.cell(w=colw,txt=f'{Describtion}',ln=True,align='L')

        #Quantity
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx+50,coly+115)
        pdf.cell(w=colw,txt=f'QUANTITY:',ln=True,align='L')

        #Quantity info
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+50,coly+125)
        pdf.cell(w=colw,txt=f'{quantity}',ln=True,align='L')

        #Price|Unit
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx+100,coly+115)
        pdf.cell(w=colw,txt=f'PRICE|UNIT:',ln=True,align='L')

        #Price|Unit info
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+100,coly+125)
        pdf.cell(w=colw,txt=f'{PriceUnit}',ln=True,align='L')

        #total Price
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx+150,coly+115)
        pdf.cell(w=colw,txt=f'TOTAL PRICE:',ln=True,align='L')

        #Total Price info
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+150,coly+125)
        pdf.cell(w=colw,txt=f'${price:,}',ln=True,align='L')
        
        
        #tax note
        if tax:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+135,coly+130)
            pdf.cell(w=colw,txt=f' Tax:',ln=True,align='L')

        #tax
        if tax:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+150,coly+130)
            pdf.cell(w=colw,txt=f'${taxnumber:,}',ln=True,align='L')
        #discount note
        if Discount:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+125,coly+135)
            pdf.cell(w=colw,txt=f'Discount:',ln=True,align='L')


        #discount
        if Discount:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+150,coly+135)
            pdf.cell(w=colw,txt=f'${Discountnumber:,}',ln=True,align='L')

        #Draw Line
        if tax or Discount or tax and Discount:
            pdf.set_line_width(0.5)#width of line
            pdf.line(colx+150,coly+138,colx+180,coly+138)

        #overall price
        if tax or Discount or tax and Discount:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+125,coly+142)
            pdf.cell(w=colw,txt=f' Overall:',ln=True,align='L')

        #Overall PRice
        if tax or Discount or tax and Discount:
            pdf.set_font(family='Courier',size=12,style='B')
            pdf.set_xy(colx+150,coly+142)
            pdf.cell(w=colw,txt=f'${OverallPrice:,}',ln=True,align='L')



        #Payment Info
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx,coly+165)
        pdf.cell(w=colw,txt=f'PAYMENT INFO',ln=True,align='L')

        #Acc name: faisa|tech
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+175)
        pdf.cell(w=colw,txt=CBankAccName,ln=True,align='L')

        #Acc Number: 509 173 1594
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+185)
        pdf.cell(w=colw,txt=CBankNumber,ln=True,align='L')

        #Bank Name: UAE Bank
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+195)
        pdf.cell(w=colw,txt=CBankName,ln=True,align='L')

        #Due:
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx,coly+205)
        pdf.cell(w=colw,txt=f'Due:',ln=True,align='L')

        #Due date
        pdf.set_font(family='Courier',size=12,style='B')
        pdf.set_xy(colx+20,coly+205)
        pdf.cell(w=colw,txt=duedate,ln=True,align='L')

        #Payment Due:
        pdf.set_font(family='Times',size=12,style='B')
        pdf.set_xy(colx+110,coly+165)
        pdf.cell(w=colw,txt=f'PAYMENT DUE:',ln=True,align='L')

        #total Price
        pdf.set_font(family='Times',size=20,style='B')
        pdf.set_xy(colx+110,coly+185)
        pdf.cell(w=colw,txt=f'${OverallPrice:,}',ln=True,align='L')


        #save PDF
        pdf_file = 'Invoice.pdf'#create the file name
        pdf.output(pdf_file)
        return pdf_file


    #store the function in a variable
    pdf_function = generate_pdf()

    #read the PDF func as binary data
    with open(pdf_function,'rb') as binary:
        pdf_data = binary.read()

    if view:
        #wrie the PDF using base64
        pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

        #Generate the Html to enbed the PDF
        pdf_enbed = f'<embed src="data:application/pdf;base64, {pdf_base64}" type="application/pdf" width="100%" height="600px" />'

        #display the embedded PDF (Markdown help us to use HTML on streamlit)
        st.markdown(pdf_enbed,unsafe_allow_html=True)

    if name and email and invoice and indate and duedate and Describtion and price and quantity:
        st.download_button(label=":blue[Download PDF]", data=pdf_data, file_name='invoice.pdf', mime='application/pdf')
    else:
        st.warning('Please Fill All Items')

if menu == 'Change Details':
    passw = '123'
    passwInput = st.sidebar.text_input('Admin Password',type='password')
    if passwInput:
        if passwInput == passw:
            st.header('Change Details')
            NewLogo = st.file_uploader('Please Upload New Logo Image',type=['png','jpg','JPEG'])
            colf1,colf2 = st.columns(2)
            with colf1:
                NewCompanyName = st.text_input('Please Enter New Company Name')
                NewCountry = st.text_input('Please Enter New Company Country')
                NewBankAccount = st.text_input('Please Enter New Company Bank Account Name')
            with colf2:
                NewCompanyAddress = st.text_input('Please Enter New Company Address')
                NewBankName = st.text_input('Please Enter New Company Bank Name')
                NewBankNumber = st.text_input('Please Enter New Bank Number')
            save = st.button('Save Changes')
            if save:
                #newData = pd.DataFrame({'Name':[NewCompanyName],'Country':[NewCountry],'Bank Account Name':[NewBankAccount],'Address':[NewCompanyAddress],'Bank Name':[NewBankName],'Bank Number':[NewBankNumber]})
                invoicedict = {}
                if NewCompanyName:
                    invoicedict['Name'] = [NewCompanyName]
                else:
                    invoicedict['Name'] = df['Name'].iloc[0]
                if NewCountry:
                    invoicedict['Country'] = [NewCountry]
                else:
                    invoicedict['Country'] = df['Country'].iloc[0]
                if NewBankAccount:
                    invoicedict['Bank Account Name'] = [NewBankAccount]
                else:
                    invoicedict['Bank Account Name'] = df['Bank Account Name'].iloc[0]
                if NewCompanyAddress:
                    invoicedict['Address'] = [NewCompanyAddress]
                else:
                    invoicedict['Address'] = df['Address'].iloc[0]
                if NewBankName:
                    invoicedict['Bank Name'] = [NewBankName]
                else:
                    invoicedict['Bank Name'] = df['Bank Name'].iloc[0]
                if NewBankNumber:
                    invoicedict['Bank Number'] = [NewBankNumber]
                else:
                    invoicedict['Bank Number'] = df['Bank Number'].iloc[0]
                invoicetable = pd.DataFrame(invoicedict)
                # #Newdf = pd.concat([df,newData],ignore_index=True)
                invoicetable.to_csv('invoice.csv',index=False)
                st.success('Data Changed')
        else:
            pass
    else:
        pass