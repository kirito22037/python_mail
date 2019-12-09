import os
import smtplib #simple mail tranfer protocol library

EMAIL_ADDRESS=os.environ.get('EMAIL_ADD')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    subject='Grab dinner this weekend?'
    body='How about at 6pm this Satuday?'

    msg=f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS,EMAIL_ADDRESS,msg)
