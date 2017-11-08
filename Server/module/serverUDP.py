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
        print('UDP - Setting up UDP server on : ' + str(self.address))
        self.cnx.bind(self.address)
        while self.run:
            (req, addr) = self.cnx.recvfrom(1024)
            print("UDP - New Client")
            self.__newClient(req, addr)
    def __newClient(self, req, addr):
        print('UDP - New Client - Sending packet to ' + str(addr))
        self.cnx.sendto( bytearray("OK" + "\t", "ascii"), addr)
