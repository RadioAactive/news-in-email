import requests
import os , time
import email_send

time = time.strftime("%d-%m-%y")

api = os.getenv("APIkey2")

url = f"https://gnews.io/api/v4/\
top-headlines?country=pk&category=general&lauguage=en\
&apikey={api}"

dic = requests.get(url)
dic = dic.json()

body = ""
for i , articles in enumerate(dic["articles"]):
    if articles["description"] == None:
        continue
    else:
        body = str(body + articles['title'] + '\n' 
        + articles['description'] + '\n' 
        + articles["url"] + 2*'\n')

# will be uploaded to a server and will be executed at a specific time

body = f"Subject: Daily news {time}\n" + body
body = body.encode("utf-8")

email_send.email_send(body)


