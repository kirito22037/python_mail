import os
import smtplib  #simple message transfer protocol library
import imghdr
from email.message import EmailMessage  #for email message formating

EMAIL_ADDRESS=os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

msg=EmailMessage()
msg['Subject']='pic attached'
msg['From']=EMAIL_ADDRESS
msg['To']=EMAIL_ADDRESS
msg.set_content('image attached >>>')

with open('pic1.jpg','rb') as f:      #file handling   and .jpg is mandatory
    file_data=f.read()                #file handling
    file_type=imghdr.what(f.name)     #with keyword closes the file automatically
    file_name=f.name                  #file handling

msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name) #all four arguments are required

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
