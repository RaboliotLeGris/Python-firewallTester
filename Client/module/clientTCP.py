import socket

class ClientTCP():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.address = (self.address, self.port)

        self.cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Then we run
        self.__run()

    def __run(self):
            self.cnx.connect(self.address)
            print('TCP - Connecting to : ' + str(self.address))
            buffer = bytearray('-Yolo-\n', 'ascii')
            self.cnx.send(buffer)
            try:
                self.cnx.settimeout(10) #Timeout of 10s
                res = self.cnx.recv(1024)
            except socket.timeout:
                print('TCP - Timed out')
            else:
                print('TCP - It Worked - ' + res.decode('ascii').strip("\n"))
            self.cnx.close()
