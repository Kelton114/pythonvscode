import streamlit as st

from email.message import EmailMessage
#set up email: sender,receiver,content
import ssl
#kepp email safe on internet so that nobody will read except receiver
import smtplib
#simple message transfer protocol tranfer protocol: this will send the mail from sender to receiver

sender = 'bot.notmain@gmail.com'
password = 'ocaglrexnuqsoxwr'

receiver = st.text_input("Enter email to send to")
subject = st.text_input('Enter email subject here')
body = st.text_area("Enter email content here",height=200)

if st.button("Send Mail"):
    email = EmailMessage() # Want to create a new message
    email['From'] = sender
    email['to'] = receiver
    email['subject'] = subject
    email.set_content(body)

    securecontent = ssl.create_default_context()# create a secure connection so no one else receives except the sender

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=securecontent) as smtp: #hostname,port,ssl
        #teh above helps us to connext to gmail server on the internet
        smtp.login(sender,password)#this login to send  email address and password
        smtp.sendmail(sender,receiver,email.as_string())#send the email to receiver as string so he can read
        st.success("Message sent. Thank You!")