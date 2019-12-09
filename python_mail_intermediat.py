import os
import smtplib #simple mail tranfer protocol library
from email.message import EmailMessage

EMAIL_ADDRESS=os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

msg=EmailMessage()
msg['Subject']='Grab dinner this weekened?'
msg['From']=EMAIL_ADDRESS
msg['To']=EMAIL_ADDRESS
msg.set_content('How about dinner at 6pm this Saturday ?')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    smtp.send_message(msg)
