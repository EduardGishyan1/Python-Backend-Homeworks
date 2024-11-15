from http.server import BaseHTTPRequestHandler,HTTPServer
from json import loads,dumps
import urllib
users = []

class Request_Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        
        email = query_params.get("email",[None])[0]
        if email:
            for user in users:
                if user.get("email") == email:
                    response_data = {"message":'user found',"user":user.get("user","Unknown")}
                    self.send_response(200)
                else:
                    response_data = {"message":'user not found'}
                    self.send_response(404)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(dumps(response_data).encode())
    
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        user_data = loads(self.rfile.read(length))
        users.append(user_data)
        response_data = {"message":"recived successfully","data":user_data}
        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()
        self.wfile.write(dumps(response_data).encode())
        

def run(server_class=HTTPServer, handler_class=Request_Handler, port=8000):
    server_address = ("127.0.0.1", port) 
    httpd = server_class(server_address, handler_class)
    print(f"Server is running on http://127.0.0.1:{port}")
    httpd.serve_forever()

run()