def show(data):
    printHeader()
    for target in data:
        printTarget(target, data[target])

def printHeader():
    line(4)
    print("| {:^15s} | {:^15s} | {:^15s} | {:^15s} |".format('Target', "IP", "Protocole/Port", "Status"))
    line(4)

def printTarget(name, data):
    for test in data:
        print("| {:^15s} | {:^15s} | {:^15s} | {:^15s} |".format(name, getIP(test), formatProtPort(test), test[3]))
        line(4)

def line(numberElem):
    toPrint = '+'
    for i in range(numberElem):
        toPrint += '-----------------+'
    print(toPrint)

def formatProtPort(data):
    return data[0] + '/' + str(data[2])

def getIP(data):
    if(data[0] == 'ICMP'):
        return data[1]
    else:
        return data[1][0]
