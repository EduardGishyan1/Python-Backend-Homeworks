import json
import random

with open("ThirdTask/company_data.json") as fs:
    data_company = json.load(fs)

name_of_employees = ["James","Bob","Ann","Emma","Alex"]
roles = ["programmer","accountant","driver","doctor","professor"]

emp_id = [j["id"] for i in data_company["departments"] for j in i["employees"]]
max_id = max(emp_id) if emp_id else 0

employees_to_add = 3

for employee_list in data_company["departments"]:
    for _ in range(employees_to_add):
        new_employee = {"id":max_id + 1,"name":random.choice(name_of_employees),"role":random.choice(roles),}
        employee_list["employees"].append(new_employee)
        max_id += 1
    
with open("ThirdTask/company_data.json","w") as fs:
    json.dump(data_company,fs,indent=2)