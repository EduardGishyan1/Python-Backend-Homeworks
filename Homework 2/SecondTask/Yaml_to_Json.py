import json 
import yaml

with open("SecondTask/data.yml",'r') as fs:
    data = yaml.load(fs,Loader=yaml.SafeLoader)

with open("SecondTask/data.json","w") as fs:
    json.dump(data,fs,indent=4)