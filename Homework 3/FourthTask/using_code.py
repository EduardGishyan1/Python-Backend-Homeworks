import requests

data = {
    "user":"James",
    "age":30,
    "name":"James",
    "email":"example.com"
}

url = "http://127.0.0.1:8000"

response = requests.post(url,json=data)
print(requests.get(url,params={"email":"example.com"}).text)
