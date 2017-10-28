import json
from io import StringIO

def loadJsonFile(path):
    # Opening json file given by the path
    # Returning a python dictionnary
    f = open(path,'r')
    fileLoaded = json.load(f)
    f.close()
    return fileLoaded
