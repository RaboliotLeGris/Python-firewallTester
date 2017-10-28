import socketserver

class TCPHandler(StreamRequestHandler):
    def handle(self):
        #Example
        buffer,socket_client = self.request
        reponse = buffer
        socket_client.send(reponse, self.client_address)

class TCPServer_Thread(ThreadingMixIn,TCPServer):
    pass

"""To run the server
with TCPServer_Thread(('0.0.0.0', 6666), TCPHandler) as serveur:
thread = threading.Thread(target = serveur.serve_forever)
thread.daemon = True
thread.start()"""
