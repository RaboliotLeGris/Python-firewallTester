import socket

class ClientTCP():
    def __init__(self, response, target, ipType, address, port):
        self.target = target
        print(self.target)
        self.address = address
        self.port = port
        self.address = (self.address, self.port)

        if ipType == 4:
            self.cnx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.cnx = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

        #Then we run
        self.__run(response)

    def __run(self, response):
            try:
                self.cnx.connect(self.address)
            except ConnectionRefusedError:
                success = 'X'
            else:
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
            response[self.target].append(('TCP', self.address, self.port, success))
