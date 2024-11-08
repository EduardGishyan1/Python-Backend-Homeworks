import json
with open("FourthTask/user_data.json") as fs:
    user_datas = json.load(fs)

filtered_data = []
required_age = 30
proffesion = "programmer"
users = user_datas["users"]

for user in users:
    if user["age"] < required_age and user["role"] == proffesion:
        filtered_data.append(user)

with open("FourthTask/filtered_users.json","w") as fs:
    json.dump({"users":filtered_data},fs,indent=2)