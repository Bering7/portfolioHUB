from library.utilities import *

def fileExists(name):
    try:
        a = open(name, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def readFile(name):
    try:
        file = open(name, 'r')
    except:
        print('Error reading file.')
    else:
        header('Registered People')
        print(file.read())