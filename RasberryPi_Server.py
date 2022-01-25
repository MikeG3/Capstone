from http.server import HTTPServer, BaseHTTPRequestHandler


#HOST = 192.168.0.42  #RasberryPI
HOST = 192.168.0.37  #Laptop
PORT = 3000

class RP_Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer((HOST, PORT), RP_Server)
httpd.serve_forever()


"""
Source
https://www.youtube.com/watch?v=hFNZ6kdBgO0&ab_channel=howCode
"""
