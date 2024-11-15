import requests

data = {
    "age":30,
    "name":"James"
}
response = requests.post("http://127.0.0.1:8000",json=data)

try:
    print(response.json())

except Exception as e:
    print(e)