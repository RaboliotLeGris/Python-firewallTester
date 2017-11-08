 #-*- coding:Utf-8 -*-

#To append the module to the path
import os
import sys
sys.path.append(os.path.realpath('module'));

import threading

#Our custom modules
from serverUDP import ServerUDP
from serverTCP import ServerTCP
import fileReader

path = './data/addresses.json'

data = fileReader.loadJsonFile(path)['data']
clients = []

print("#### Starting clients : ####")
for toPing in data:
    if toPing['protocole'] == 'TCP':
        print('TCP')
        servers.append(threading.Thread(target=ClientTCP, args = [toPing['port']]))
    elif toPing['protocole'] == 'UDP':
        print('UDP')
        servers.append(threading.Thread(target=ClientUDP, args = [toPing['port']]))
    elif toPing['protocole'] == 'ICMP':
        print('ICMP - Not implemented')
    else:
        print('Unsupported protocole' + toPing['protocole'])

for client in clients:
    client.start()

#Managing the end of the thread exec (That should never happened)
for client in clients:
    client.join()
print('Over')
