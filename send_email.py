import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465

    my_email = EMAIL_USER
    password = EMAIL_PASS

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(my_email, password)
        server.sendmail(my_email, my_email, user_message)