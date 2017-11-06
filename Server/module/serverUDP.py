import socket
import threading

class ServerUDP():
    def __init__(self, port):
        self.run = True
        self.port = port

        self.address = ('0.0.0.0', self.port)
        self.cnx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #Then we run
        self.__run()

    def __run(self):
        cnx.bind(self.address)
        while self.run:
            (req, addr) = cnx.recvfrom(1024)
            # We could stock each thread + infos, but it won't be useful
            threading.Thread(target=self.__newClient, args = [req, addr]).start()
    def __newClient(self, req, addr):
        self.__send(addr) # Not really useful but it look nicer
    def __send(self):
        self.cnx.sendto( bytearray("OK" + "\t", "ascii"), addr)
