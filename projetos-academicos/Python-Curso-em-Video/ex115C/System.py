from library.utilities import *
from library.file import *

file = 'ex115C/cursoemvideo.txt'
if not fileExists(file):
    with open(file, 'w') as file:
        file.write('')
    print('File created successfully!')

while True:
    answer = menu(['View Registred Users', 'Register a New User', 'Log Out'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        registerUser(file)
    elif answer == 3:
        header('Logging Out... See you later!')
        break
    else:
        header('ERRO! Enter an valid option!')