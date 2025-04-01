import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8085

def resource_path(relative_path):
    """Get path to resource (works for PyInstaller)"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.abspath(relative_path)


def open_browser():
    webbrowser.open(f"http://localhost:{PORT}")

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/shutdown':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Server shutting down...")
            threading.Thread(target=self.server.shutdown, daemon=True).start()
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/shutdown':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Server shutting down (POST)...")
            threading.Thread(target=self.server.shutdown, daemon=True).start()
        else:
            self.send_error(404)


def start_server():
    asset_dir = resource_path("build")  # assuming you used --add-data "build;build"
    os.chdir(asset_dir)
    handler = MyHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        open_browser()
        httpd.serve_forever()

thread = threading.Thread(target=start_server, daemon=True)
thread.start()
try:
    while thread.is_alive():
        thread.join(1)
except KeyboardInterrupt:
    print("Exiting...")