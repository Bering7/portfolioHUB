from library.utilities import *

while True:
    answer = menu(['View Registred Users', 'Register a New User', 'Log Out'])
    if answer == 1:
        header('Option 1')
    elif answer == 2:
        header('Option 2')
    elif answer == 3:
        header('Logging Out... See you later!')
        break
    else:
        header('ERRO! Enter an valid option!')