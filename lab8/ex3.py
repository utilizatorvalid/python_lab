# 3. Sa se porneasca un server care sa expuna fisierele si directoarele din directorul curent. Accesati acel server
# dintr-un browser, si apoi folosind un client HTTP in python (urllib.request)
from http.server import HTTPServer, SimpleHTTPRequestHandler

server_adress = ('127.0.0.1',6996)

httpd = HTTPServer(server_adress,SimpleHTTPRequestHandler)
httpd.serve_forever()