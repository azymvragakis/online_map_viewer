"""
Simple local server to test the map
Run this and open http://localhost:8000 in your browser
"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Change to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def log_message(self, format, *args):
        # Add more detailed logging for debugging
        super().log_message(format, *args)

Handler = CORSRequestHandler

print(f"🌍 Starting server at http://localhost:{PORT}")
print(f"📂 Serving files from: {os.getcwd()}")
print(f"\n✨ Opening browser...")
print(f"\nPress Ctrl+C to stop the server\n")

# Open browser automatically
webbrowser.open(f'http://localhost:{PORT}')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
