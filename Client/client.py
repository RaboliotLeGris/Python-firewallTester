 #-*- coding:Utf-8 -*-

#To append the module to the path
import os
import sys
sys.path.append(os.path.realpath('module'));

import threading

#Our custom modules
from clientUDP import ClientUDP
from clientTCP import ClientTCP
import fileReader

path = './data/addresses.json'

data = fileReader.loadJsonFile(path)['data']
clients = []

# TODO :
# Get value from the threads
# Generate table at the end


print("#### Starting clients : ####")
for toPing in data:
    if toPing['protocole'] == 'TCP':
        clients.append(threading.Thread(target=ClientTCP, args = [toPing['address'], toPing['port']]))
    elif toPing['protocole'] == 'UDP':
        clients.append(threading.Thread(target=ClientUDP, args = [toPing['address'], toPing['port']]))
    elif toPing['protocole'] == 'ICMP':
        print('ICMP - Not implemented yet')
    else:
        print('Unsupported protocole' + ' - ' + toPing['address'] + ' - ' + toPing['protocole'])

for client in clients:
    client.start()

#Managing the end of the thread exec (That should never happened)
for client in clients:
    client.join()
print('Over')
