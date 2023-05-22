import smtplib
import os

email_id = os.environ.get("EMAIL_ADDR")
email_pass = os.environ.get("EMAIL_PASS")

# 587 is a port number
with smtplib.SMTP('smtp.gmail.com',587) as smtp: 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email_id,email_pass)

    subject = 'Fight Against Corona Virus'
    body = "Hey, hello lets fight against corona virus"

    msg = f'Subject: {subject}\n\n\n{body}'
    smtp.sendmail(email_id, 'priyanshujain09062003@gmail.com',msg)
    