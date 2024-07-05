import requests
import os
import email_send

api = os.getenv("APIkey2")

url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={api}"

dic = requests.get(url)
dic = dic.json()

body = ""
for i , articles in enumerate(dic["articles"]):
    if articles["description"] == None:
        continue
    else:
        body = str(body + articles['title'] + '\n' + articles['description'] + '\n\n')

body = body.encode("utf-8")

email_send.email_send(body)


