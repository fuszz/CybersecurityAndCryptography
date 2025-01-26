from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        # Print the request method
        print(f"Method: {self.command}")

        # Print response headers for CORS
        self.send_response(200)
        self.send_header('Allow', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        # Print the request method
        print(f"Method: {self.command}")

        # Print the request body
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            body = self.rfile.read(content_length)
            print(f"Body: {body.decode('utf-8')}")
        else:
            print("Body: None")

        # Send a response for the POST request
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({"status": "success"})
        self.wfile.write(response.encode('utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')

if __name__ == "__main__":
    server = HTTPServer(('127.0.0.1', 9999), MyHandler)
    print("Server started on http://127.0.0.1:9999")
    server.serve_forever()

