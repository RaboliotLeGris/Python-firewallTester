 #-*- coding:Utf-8 -*-

#To append the module to the path
import os
import sys
sys.path.append(os.path.realpath('module'));

import threading

#Our custom modules
from clientUDP import ClientUDP
from clientTCP import ClientTCP
from clientICMP import ClientICMP
import display
import fileReader

path = './data/addresses.json'

data = fileReader.loadJsonFile(path)['data']
for i in data:
    print(data[i])

responses = {}
clients = []

# TODO :
# Display the data


print("#### Starting clients : ####")
for target in data:
    responses[target] = [] #A bit unordered
    for toPing in data[target]:
        if toPing['protocole'] == 'TCP':
            clients.append(threading.Thread(target=ClientTCP, args = [responses, target, toPing['address'], toPing['port']]))
        elif toPing['protocole'] == 'UDP':
            clients.append(threading.Thread(target=ClientUDP, args = [responses, target, toPing['address'], toPing['port']]))
        elif toPing['protocole'] == 'ICMP':
            clients.append(threading.Thread(target=ClientICMP, args=[responses, target, toPing['address']]))
        else:
            print('Unsupported protocole' + ' - ' + toPing['address'] + ' - ' + toPing['protocole'])

for client in clients:
    client.start()

#Managing the end of the thread exec (That should never happened)
for client in clients:
    client.join()
print('#### Over ####')
display.show(responses)
