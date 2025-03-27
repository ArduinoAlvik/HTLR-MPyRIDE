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

def start_server():
    asset_dir = resource_path("build")  # assuming you used --add-data "build;build"
    os.chdir(asset_dir)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at http://localhost:{PORT}")
        open_browser()
        httpd.serve_forever()

threading.Thread(target=start_server).start()
