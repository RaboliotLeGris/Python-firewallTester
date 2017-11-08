import socket

class ClientUDP():
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.address = (self.address, self.port)

        self.cnx = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #Then we run
        self.__run()

    def __run(self):
        print('UDP - Connecting to : ' + str(self.address))
        buffer = bytearray('-Yolo-\n', 'ascii')
        self.cnx.sendto(buffer, self.address)
        try:
            self.cnx.settimeout(10) #Timeout of 10s
            (res,addr) = self.cnx.recvfrom(1024)
        except socket.timeout:
            print('time out')
        else:
            print('UDP - It Worked - ' + res.decode('ascii').strip("\n"))
