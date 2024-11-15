from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from json import loads,dumps
users = []

class Request_Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b'''
        <html>
            <body>
                <h1>GET request received</h1>
            </body>
        </html>
        ''')
    
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