import requests
import json

url = "https://jsonplaceholder.typicode.com/posts?id=1"
response = requests.get(url)

with open("FifthTask/data.json",'+w') as fs:
    if response.status_code == 200:
        response_content = response.json()
        for di in response_content:
            json.dump({"title":di["title"]},fs)
