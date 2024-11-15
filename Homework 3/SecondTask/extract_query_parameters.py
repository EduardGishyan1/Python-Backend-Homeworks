class Handler:
    def __init__(self,path:str):
        self.path = path
    
    def extract_query_parameters(self,param_name):
        if not "?" in self.path:
            return None
                
        separate = self.path.split("?")
        for i in separate:
            deep_separate = i.split("&")
            for j in deep_separate:
                if "=" in j:
                    key,value = j.split("=",1) 

                    if key == param_name:
                        return value
                
url = "/somepage?name=JaneDoe&email=janedoe@example.com&age=30"          
param_name = "email"
Handler_object = Handler(url)
value = Handler_object.extract_query_parameters(param_name)
print(value)