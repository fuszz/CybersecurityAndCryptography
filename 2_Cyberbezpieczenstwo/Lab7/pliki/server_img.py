import http.server
import socketserver

# Define the port on which the server will run
PORT = 8888

# Create a custom request handler to serve SVG images
class SVGHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'image/svg+xml')  # Set the content type to SVG
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        # Print the HTTP request headers
        print("HTTP Request Headers:")
        for header, value in self.headers.items():
            print(f"{header}: {value}")

        # Call the parent class's do_GET to serve the SVG file
        http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create a socket server with the custom request handler
with socketserver.TCPServer(("0.0.0.0", PORT), SVGHandler) as httpd:
    print(f"Serving on port {PORT}")
    # Start the server
    httpd.serve_forever()

