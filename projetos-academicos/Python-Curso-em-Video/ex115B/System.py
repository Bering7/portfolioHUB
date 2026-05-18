from library.utilities import *
from library.file import *

file = 'ex115B/cursoemvideo.txt'
if fileExists(file):
    print('File already exists.')
else:
    with open(file, 'w') as file:
        file.write('')
    print('File created successfully!')

while True:
    answer = menu(['View Registred Users', 'Register a New User', 'Log Out'])
    if answer == 1:
        readFile(file)
    elif answer == 2:
        header('Option 2')
    elif answer == 3:
        header('Logging Out... See you later!')
        break
    else:
        header('ERRO! Enter an valid option!')