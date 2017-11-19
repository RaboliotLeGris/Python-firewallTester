import socket
import threading

class ServerTCP():
    def __init__(self, ipType, port):
        self.run = True
        self.port = port

        if ipType == 4:
            self.address = ('0.0.0.0', self.port)
            self.cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.address = ('::', self.port)
            self.cnx = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

        #Then we run
        self.__run()

    def __run(self):
        print('TCP - Setting up TCP server on : ' + str(self.address))
        self.cnx.bind(self.address)
        self.cnx.listen(100)
        while self.run:
            temp = self.cnx
            (client, addr) = temp.accept()
            # We could stock each thread + infos, but it won't be useful
            threading.Thread(target=self.__newClient, args = [client, addr]).start()
    def __newClient(self, client, addr):
        print('TCP - New Client - Sending packet to ' + str(addr))
        data = client.recv(1024).decode('ascii').strip("\n")
        self.__send(client)
        print("TCP - Connection closed")
        client.close()
    def __send(self, client):
        #try: #It was throwing an annoying and useless error
        client.send(bytearray('OK\n', 'ascii'))
        #except:
        #    pass
