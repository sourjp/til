import http.server
import socketserver

with socketserver.TCPServer(
    ('127.0.0.1', 8000),http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()



'''
import webbrowser
url = 'http://127.0.0.1:8000'
webbrowser.open(url)

f = webbrowser.get('firefox')
f.open(url)
'''