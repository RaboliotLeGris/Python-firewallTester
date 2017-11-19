 #-*- coding:Utf-8 -*-

#To append the module to the path
import os
import sys
sys.path.append(os.path.realpath('module'));

#
import threading

#Our custom modules
from serverUDP import ServerUDP
from serverTCP import ServerTCP
import fileReader

path = './data/ports.json'

data = fileReader.loadJsonFile(path)['data']
servers = []

print("#### Starting servers : ####")
for toListen in data:
    if toListen['protocole'] == 'TCP':
        print('TCP')
        servers.append(threading.Thread(target=ServerTCP, args = [toListen['IPv'], toListen['port']]))
    elif toListen['protocole'] == 'UDP':
        print('UDP')
        servers.append(threading.Thread(target=ServerUDP, args = [toListen['IPv'], toListen['port']]))
    else:
        print('Unsupported protocole' + toListen['protocole'])

for server in servers:
    server.start()

#Managing the end of the thread exec (That should never happened)
for server in servers:
    server.join()
print('Over')
