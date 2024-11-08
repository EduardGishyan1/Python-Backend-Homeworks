import yaml
with open("FirstTask/config.yml","r+") as fs:
    data = yaml.load(fs,Loader=yaml.SafeLoader)

data["server"]["port"] = 9090

with open("FirstTask/config.yml","w") as fs:
    yaml.dump(data,fs,default_flow_style=False,allow_unicode=True,indent=4)
