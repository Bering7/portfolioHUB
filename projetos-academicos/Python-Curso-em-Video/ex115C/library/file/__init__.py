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
    header('Registered People')
    try:
        with open(name, 'rt', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(';')
                print(f'{data[0]:<50}{data[1].replace(';', ''):>3}')
    except:
        print('Error reading file.')

def registerUser(file):
    header('Registering a New User')
    name = input('Name: ').title()
    age = input('Age: ')
    try:
        with open(file, 'a', encoding='utf-8') as f:
            f.write(f'{name};{age} years\n')
    except:
        print('Error registering new user.')
    else:
        print('User registered successfully!')