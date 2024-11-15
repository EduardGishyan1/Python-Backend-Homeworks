import requests

url = "http://127.0.0.1:8000"
request = requests.post(url)
with open("index.html","w") as fs:
    fs.write(request.content.decode())