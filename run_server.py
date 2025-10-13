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

Handler = http.server.SimpleHTTPRequestHandler

print(f"🌍 Starting server at http://localhost:{PORT}")
print(f"📂 Serving files from: {os.getcwd()}")
print(f"\n✨ Opening browser...")
print(f"\nPress Ctrl+C to stop the server\n")

# Open browser automatically
webbrowser.open(f'http://localhost:{PORT}')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
