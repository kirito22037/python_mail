import os
import smtplib #simple mail tranfer protocol library

EMAIL_ADDRESS=os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

with smtplib.SMTP('localhost',1025) as smtp:

    subject='Grab dinner this weekend?'
    body='How about at 6pm this Satuday?'

    msg=f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
