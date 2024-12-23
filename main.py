import requests
from dotenv import load_dotenv
import os
from send_email import send_email

load_dotenv()
API_KEY = os.getenv('API_KEY')

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

topic = "tesla"
url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       f"sortBy=publishedAt&"
       f"apiKey={API_KEY}&"
       f"language=en")

get_request = requests.get(url)
content = get_request.json()

body = "Subject: What happened today!\n"
for article in content["articles"][:20]:
    body = body + f'{article["title"]}\n{article["description"]}\n{article["url"]}\n\n'

user_message = body.encode('utf-8')
send_email(user_message)

