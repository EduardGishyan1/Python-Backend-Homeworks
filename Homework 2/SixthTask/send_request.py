import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

with open("SixthTask/json_for_send.json") as fs:
    json_content = json.load(fs)

response = requests.post(url,json=json_content)

if response.status_code == 201:
    print(response.json())
else:
    print("fail")