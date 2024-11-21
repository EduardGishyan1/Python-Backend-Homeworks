from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
]

class CRUDHandler(BaseHTTPRequestHandler):
    def __set_headers(self, status=200):
        """Set common response headers."""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def __path_parser(self):
        """Parse the URL path."""
        parsed_path = self.path.strip('/').split('/')
        return parsed_path

    def do_GET(self):
        """Handle GET requests."""
        parsed_path = self.__path_parser()
        
        if len(parsed_path) == 1:
            if parsed_path[0] == 'users':
                self.__set_headers()
                self.wfile.write(json.dumps(users).encode())
            elif parsed_path[0] == 'products':
                self.__set_headers()
                self.wfile.write(json.dumps(products).encode())
            else:
                self.__set_headers(400)
                self.wfile.write(json.dumps({'error': 'path not found...'}).encode())
        elif len(parsed_path) == 2:
            resource, resource_id = parsed_path
            if resource == 'users':
                result = next((u for u in users if u['id'] == int(resource_id)), None)
            elif resource == 'products':
                result = next((p for p in products if p['id'] == int(resource_id)), None)
            else:
                result = None
            
            if result:
                self.__set_headers()
                self.wfile.write(json.dumps(result).encode())
            else:
                self.__set_headers(404)
                self.wfile.write(json.dumps({'error': 'Not found...'}).encode())
        else:
            self.__set_headers(404)
            self.wfile.write(json.dumps({'error': 'not found...'}).encode())

    def do_POST(self):
        """Handle POST requests."""
        parsed_path = self.__path_parser()

        if len(parsed_path) == 1:
            resource = parsed_path[0]
            content_length = int(self.headers['Content-length'])
            body = json.loads(self.rfile.read(content_length))

            if resource == 'users':
                new_id = max([u['id'] for u in users], default=0) + 1
                body['id'] = new_id
                users.append(body)
                self.__set_headers()
                self.wfile.write(json.dumps(users).encode())
            elif resource == 'products':
                new_id = max([p['id'] for p in products], default=0) + 1
                body['id'] = new_id
                products.append(body)
                self.__set_headers()
                self.wfile.write(json.dumps(products).encode())
            else:
                self.__set_headers(404)
                self.wfile.write(json.dumps({'error': 'Invalid resource'}).encode())
        else:
            self.__set_headers(404)
            self.wfile.write(json.dumps({'error': 'Invalid request'}).encode())

    def do_DELETE(self):
        """Handle DELETE requests."""
        parsed_path = self.__path_parser()

        if len(parsed_path) == 2:
            resource, resource_id = parsed_path
            resource_id = int(resource_id)
            if resource == 'users':
                user_to_delete = next((u for u in users if u['id'] == resource_id), None)
                if user_to_delete:
                    users.remove(user_to_delete)
                    self.__set_headers()
                    self.wfile.write(json.dumps({"message": "User deleted successfully"}).encode())
                else:
                    self.__set_headers(404)
                    self.wfile.write(json.dumps({"error": "User not found"}).encode())
            elif resource == 'products':
                product_to_delete = next((p for p in products if p['id'] == resource_id), None)
                if product_to_delete:
                    products.remove(product_to_delete)
                    self.__set_headers()
                    self.wfile.write(json.dumps({"message": "Product deleted successfully"}).encode())
                else:
                    self.__set_headers(404)
                    self.wfile.write(json.dumps({"error": "Product not found"}).encode())
            else:
                self.__set_headers(404)
                self.wfile.write(json.dumps({"error": "Invalid resource"}).encode())
        else:
            self.__set_headers(404)
            self.wfile.write(json.dumps({"error": "Invalid id or endpoint"}).encode())

def run(server_class=HTTPServer, server_handler=CRUDHandler, port=8000):
    """Run the HTTP server."""
    server_address = ('', port)
    httpd = server_class(server_address, server_handler)

    print(f"Server running on port: {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
