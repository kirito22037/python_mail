import os
import smtplib
from email.message import EmailMessage

#getting email and password  for this app from environment key
EMAIL_ADDRESS=os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

msg=EmailMessage()
msg['Subject']='pdf is attached'
msg['From']=EMAIL_ADDRESS
msg['To']=EMAIL_ADDRESS
msg.set_content('this is an eg of attching a pdf')

#file handling
f=open('RoadSense.pdf','rb')
file_data=f.read()
file_name=f.name

f.close()

msg.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=file_name)

#connecting with gmail , login and send
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)
