import subprocess

class ClientICMP():
    def __init__(self, response, address):
        self.address = address
        self.__run(response)

    def __run(self, response):
        result = subprocess.run(['ping', '-c', '1', self.address])
        if(result.returncode == 0):
            success = 'OK'
        else:
            success = 'X'
        response.append(('ICMP', self.address, 0, success))
