##food,recyling, donations, loan

#https://stemhackathon.com/question-10-pro

import streamlit as st
from fpdf import FPDF
import base64

menu = st.sidebar.selectbox('Menu',['Food','Recycyling','Donations','Loan','Liam Football Thing'])
if menu == 'Food':
    st.header('Good Taste Resturant')
    st.write('------')
    cola1,cola2 = st.columns(2)
    with cola1:
        Food_Name1 = st.text_input('Please Enter Food Name')
    with cola2:
        colaa1,colaa2 = st.columns(2)
        with colaa1:
            Price1 = st.number_input('Price :',0.00)
        with colaa2:
            Quantity1 = st.number_input('Quantity :',0)
            totalPrice = Price1*Quantity1

    view = st.button(':blue[View Food Ordered]')
    def generate_pdf():
        pdf = FPDF()

        #Add a page
        pdf.add_page()

        #set your default fonts
        pdf.set_font('Arial',size=12)

        colx = 20
        coly = 20
        colw= 90

        #FONTS: Courier, Arial, Times, Symbol

        #Name
        pdf.set_font(family='Times',size=25,style='B')
        pdf.set_xy(colx,coly+5)
        pdf.cell(w=colw,txt='Good Taste Resturant',ln=True,align='L')

        #Food Ordered
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+25)
        pdf.cell(w=colw,txt='Food Ordered :',ln=True,align='L')

        #Food
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+35)
        pdf.cell(w=colw,txt=f'{Food_Name1}',ln=True,align='L')


        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+25)
        pdf.cell(w=colw,txt='Price :',ln=True,align='L')

        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+35)
        pdf.cell(w=colw,txt=f'{Price1:,}',ln=True,align='L')

        #Quantity
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+100,coly+25)
        pdf.cell(w=colw,txt='Quantity :',ln=True,align='L')

        #Quantity
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+100,coly+35)
        pdf.cell(w=colw,txt=f'{Quantity1:,}',ln=True,align='L')

        #Total Price
        pdf.set_font(family='Times',size=20,style='B')
        pdf.set_xy(colx,coly+50)
        pdf.cell(w=colw,txt=f'Total Price :',ln=True,align='L')

        #Total Price
        pdf.set_font(family='Times',size=18,style='B')
        pdf.set_xy(colx,coly+65)
        pdf.cell(w=colw,txt=f'${totalPrice:,}',ln=True,align='L')

        #Draw Line
        pdf.set_line_width(0.5)#width of line
        pdf.line(colx,coly+40,colx+180,coly+40)


        #save PDF
        pdf_file = 'Food.pdf'#create the file name
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

if menu == 'Recycyling':
    st.header('Good Guy Recycling Company')
    st.write('------')
    cola1,cola2 = st.columns(2)
    with cola1:
        Recycling_Name = st.text_input('Please Enter Things Recycled')
    with cola2:
        Quantity2 = st.number_input('Quantity :',0)


    view = st.button(':blue[View Recycle Record]')
    def generate_pdf():
        pdf = FPDF()

        #Add a page
        pdf.add_page()

        #set your default fonts
        pdf.set_font('Arial',size=12)

        colx = 20
        coly = 20
        colw= 90

        #FONTS: Courier, Arial, Times, Symbol

        #Name
        pdf.set_font(family='Times',size=25,style='B')
        pdf.set_xy(colx,coly+5)
        pdf.cell(w=colw,txt='Good Guy Recycling Company',ln=True,align='L')

        #Recycle
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+25)
        pdf.cell(w=colw,txt='Things Recycled :',ln=True,align='L')

        #Food
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+35)
        pdf.cell(w=colw,txt=f'{Recycling_Name}',ln=True,align='L')


        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+25)
        pdf.cell(w=colw,txt='Quantity',ln=True,align='L')

        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+35)
        pdf.cell(w=colw,txt=f'{Quantity2:,}',ln=True,align='L')


        #save PDF
        pdf_file = 'Food.pdf'#create the file name
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

if menu == 'Donations':
    st.header('Good Dude Donation')
    st.write('------')
    cola1,cola2 = st.columns(2)
    with cola1:
        Donator_Name = st.text_input('Please Enter Donator Name')
    with cola2:
         DonateAmout = st.number_input('Amount :',0.00)

    view = st.button(':blue[View Donation Reocord]')
    def generate_pdf():
        pdf = FPDF()

        #Add a page
        pdf.add_page()

        #set your default fonts
        pdf.set_font('Arial',size=12)

        colx = 20
        coly = 20
        colw= 90

        #FONTS: Courier, Arial, Times, Symbol

        #Name
        pdf.set_font(family='Times',size=25,style='B')
        pdf.set_xy(colx,coly+5)
        pdf.cell(w=colw,txt='Good Dude Donation',ln=True,align='L')

        #Food Ordered
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+25)
        pdf.cell(w=colw,txt='Donator :',ln=True,align='L')

        #Food
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+35)
        pdf.cell(w=colw,txt=f'{Donator_Name}',ln=True,align='L')


        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+25)
        pdf.cell(w=colw,txt='Amount :',ln=True,align='L')

        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+35)
        pdf.cell(w=colw,txt=f'${DonateAmout:,}',ln=True,align='L')

        

        #Total Price
        pdf.set_font(family='Times',size=18,style='B')
        pdf.set_xy(colx,coly+65)
        pdf.cell(w=colw,txt=f'Thank You Very Much !!',ln=True,align='L')




        #save PDF
        pdf_file = 'Food.pdf'#create the file name
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

if menu == 'Loan':
    st.header('Poor Person Donation')
    st.write('------')
    cola1,cola2 = st.columns(2)
    with cola1:
        GuyWhoLoan_Name = st.text_input('Please Enter Name of The Person Who wants a loan')
    with cola2:
         LoanAmout = st.number_input('Amount :',0.00)

    view = st.button(':blue[View Loan]')
    def generate_pdf():
        pdf = FPDF()

        #Add a page
        pdf.add_page()

        #set your default fonts
        pdf.set_font('Arial',size=12)

        colx = 20
        coly = 20
        colw= 90

        #FONTS: Courier, Arial, Times, Symbol

        #Name
        pdf.set_font(family='Times',size=25,style='B')
        pdf.set_xy(colx,coly+5)
        pdf.cell(w=colw,txt='Poor Person Donation',ln=True,align='L')

        #Food Ordered
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+25)
        pdf.cell(w=colw,txt='Person Who Loan :',ln=True,align='L')

        #Food
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx,coly+35)
        pdf.cell(w=colw,txt=f'{GuyWhoLoan_Name}',ln=True,align='L')


        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+25)
        pdf.cell(w=colw,txt='Amount :',ln=True,align='L')

        #Price
        pdf.set_font(family='Courier',size=15,style='B')
        pdf.set_xy(colx+60,coly+35)
        pdf.cell(w=colw,txt=f'${LoanAmout:,}',ln=True,align='L')

        

        #Total Price
        pdf.set_font(family='Times',size=18,style='B')
        pdf.set_xy(colx,coly+65)
        pdf.cell(w=colw,txt=f'Remember to return the loan amount on time after use',ln=True,align='L')




        #save PDF
        pdf_file = 'Food.pdf'#create the file name
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

if menu == 'Liam Football Thing':
    LoginName = 'Liam'
    Pass = '123'
    LogName = st.sidebar.text_input('Login Name:')
    Password = st.sidebar.text_input('Password',type='password')
    Login = st.sidebar.checkbox('Login')
    if Login:
        if LogName and Password:
            if LogName == LoginName and Password == Pass:
                st.header('Liam Football Thing')
                colb1,colb2,colb3,colb4 = st.columns(4)
                with colb1:
                    ticket = st.text_input('Item :',placeholder='Match Tickets',disabled=True)
                with colb2:
                    TikPrice = 100
                    PricePerTick = st.text_input('Price Per Ticket :',disabled=True,placeholder=f'${TikPrice}')
                with colb3:
                    TikQuantity = st.number_input('Quantity:',0)
                with colb4:
                    TikTotalPrice = TikQuantity*TikPrice
                    TikOverPrice = st.text_input('Total Price Per Item',disabled=True,placeholder=f'${TikTotalPrice}')
                
                
                colc1,colc2,colc3,colc4 = st.columns(4)
                with colc1:
                    Jersey = st.text_input('sfsfsfsffff',placeholder='Jersey',disabled=True,label_visibility='hidden')
                with colc2:
                    JerseyPrice = 60
                    PricePerJersey = st.text_input('tufgv',disabled=True,placeholder=f'${JerseyPrice}',label_visibility='hidden')
                with colc3:
                    JerseyQuantity = st.number_input('dsdsdsdsdsd',0,label_visibility='hidden')
                with colc4:
                    JerseyTotalPrice = JerseyQuantity*JerseyPrice
                    JerseyOverPrice = st.text_input('sfsf',disabled=True,placeholder=f'${JerseyTotalPrice}',label_visibility='hidden')

                cold1,cold2,cold3,cold4 = st.columns(4)
                with cold1:
                    Scarf = st.text_input('sfsfsfsfff',placeholder='Scarf',disabled=True,label_visibility='hidden')
                with cold2:
                    ScarfPrice = 30
                    PricePerScarf = st.text_input('tufg',disabled=True,placeholder=f'${ScarfPrice}',label_visibility='hidden')
                with cold3:
                    ScarfQuantity = st.number_input('dsdsdsddsd',0,label_visibility='hidden')
                with cold4:
                    ScarfTotalPrice = ScarfQuantity*ScarfPrice
                    ScarfOverPrice = st.text_input('sff',disabled=True,placeholder=f'${ScarfTotalPrice}',label_visibility='hidden')

                cole1,cole2,cole3,cole4 = st.columns(4)
                with cole1:
                    Hat = st.text_input('sfsfsefsfff',placeholder='Hat',disabled=True,label_visibility='hidden')
                with cole2:
                    HatPrice = 20
                    PricePerHat = st.text_input('tuefg',disabled=True,placeholder=f'${HatPrice}',label_visibility='hidden')
                with cole3:
                    HatQuantity = st.number_input('dsdesdsddsd',0,label_visibility='hidden')
                with cole4:
                    HatTotalPrice = HatQuantity*HatPrice
                    HatOverPrice = st.text_input('sfef',disabled=True,placeholder=f'${HatTotalPrice}',label_visibility='hidden')

                colf1,colf2,colf3,colf4 = st.columns(4)
                with colf1:
                    Popcorn = st.text_input('sfsfrrrrrsesfff',placeholder='Popcorn',disabled=True,label_visibility='hidden')
                with colf2:
                    PopcornPrice = 10
                    PricePerPopcorn = st.text_input('teeeeefg',disabled=True,placeholder=f'${PopcornPrice}',label_visibility='hidden')
                with colf3:
                    PopcornQuantity = st.number_input('dsdestttttsddsd',0,label_visibility='hidden')
                with colf4:
                    PopcornTotalPrice = PopcornQuantity*PopcornPrice
                    PopcornOverPrice = st.text_input('sdddddff',disabled=True,placeholder=f'${PopcornTotalPrice}',label_visibility='hidden')

                colg1,colg2,colg3,colg4 = st.columns(4)
                with colg1:
                    Hotdog = st.text_input('sfsfrrrrrgsesfff',placeholder='Hotdog',disabled=True,label_visibility='hidden')
                with colg2:
                    HotdogPrice = 15
                    PricePerHotdog = st.text_input('teegeeefg',disabled=True,placeholder=f'${HotdogPrice}',label_visibility='hidden')
                with colg3:
                    HotdogQuantity = st.number_input('dsdesgtttttsddsd',0,label_visibility='hidden')
                with colg4:
                    HotdogTotalPrice = HotdogQuantity*HotdogPrice
                    HotdogOverPrice = st.text_input('sddgdddff',disabled=True,placeholder=f'${HotdogTotalPrice}',label_visibility='hidden')

                colh1,colh2,colh3,colh4 = st.columns(4)
                with colh1:
                    Soda = st.text_input('sfsfrrrrhgsesfff',placeholder='Soda',disabled=True,label_visibility='hidden')
                with colh2:
                    SodaPrice = 5
                    PricePerSoda = st.text_input('teeheeefg',disabled=True,placeholder=f'${SodaPrice}',label_visibility='hidden')
                with colh3:
                    SodaQuantity = st.number_input('dsdeshtttttsddsd',0,label_visibility='hidden')
                with colh4:
                    SodaTotalPrice = SodaQuantity*SodaPrice
                    SodaOverPrice = st.text_input('sddhdddff',disabled=True,placeholder=f'${SodaTotalPrice}',label_visibility='hidden')

                coli1,coli2 = st.columns(2)
                with coli1:
                    Passs = st.radio('Pass Choice',['Standard Pass','VIP Pass'],horizontal=True)
                    standard = 200
                    VIPprice = 500
                with coli2:
                    if Passs =='Standard Pass':
                        PassPrice = st.text_input('Price:',disabled=True,placeholder=f'${standard}')
                        PPrice = standard
                    else:
                        PassPrice = st.text_input('Price:',disabled=True,placeholder=f'${VIPprice}')
                        PPrice = VIPprice

                colj1,colj2 = st.columns(2)
                with colj1:
                    subscription = st.radio('Subscription Choice',['Monthly','Annual'],horizontal=True)
                    Monthly = 20
                    Annual = 200
                with colj2:
                    if subscription =='Monthly':
                        sPrice = st.text_input('Prddice:',disabled=True,placeholder=f'${Monthly}',label_visibility='hidden')
                        SubPrice = Monthly
                    else:
                        sPrice = st.text_input('Priddce:',disabled=True,placeholder=f'${Annual}',label_visibility='hidden')
                        SubPrice = Annual
                st.subheader('Total Price:')
                total = TikTotalPrice+HatTotalPrice+SodaTotalPrice+ScarfTotalPrice+HotdogTotalPrice+PopcornTotalPrice+JerseyTotalPrice+PPrice+SubPrice
                st.subheader(f'${total}')
            else:
                st.warning('Wrong Login Name or Password')
        else:
            st.warning('Plese Enter Login Information')