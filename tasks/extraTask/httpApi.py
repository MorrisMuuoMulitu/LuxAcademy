from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import socketserver

class myhandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if  self.path=='/myotherpage':
            self.path='myotherpage.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 5000

Handler = myhandler()

myserver = socketserver.TCPServer(("", PORT), Handler)
myserver.serve_forever()
print("Server started on port"+str(PORT))
myserver.serve_forever()
