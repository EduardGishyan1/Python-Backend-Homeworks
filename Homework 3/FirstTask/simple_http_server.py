from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class SimpleRequestHandler(BaseHTTPRequestHandler):
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
        length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(length)
        post_data = urllib.parse.parse_qs(post_data.decode('utf-8'))

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f'''
        <html><body>
        <h2>POST Request Received</h2>
        </body></html>
        '''.encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleRequestHandler, port=8000):
    server_address = ("127.0.0.1", port) 
    httpd = server_class(server_address, handler_class)
    print(f"Server is running on http://127.0.0.1:{port}")
    httpd.serve_forever()

run()