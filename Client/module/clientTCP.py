import socket

class ClientTCP():
    def __init__(self, response, address, port):
        self.address = address
        self.port = port
        self.address = (self.address, self.port)

        self.cnx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Then we run
        self.__run(response)

    def __run(self, response):
            self.cnx.connect(self.address)
            print('TCP - Connecting to : ' + str(self.address))
            buffer = bytearray('-Yolo-\n', 'ascii')
            self.cnx.send(buffer)
            try:
                self.cnx.settimeout(10) #Timeout of 10s
                res = self.cnx.recv(1024)
            except socket.timeout:
                success = 'X'
                print('TCP - Timed out')
            else:
                success = 'OK'
                print('TCP - It Worked - ' + res.decode('ascii').strip("\n"))
            response.append(('TCP', self.address, self.port, success))
