while True:
    print('~' *40)
    print(f'{"PYHelp System":^40}')
    print('~' *40)
    opition = str(input('Function or library: ')).strip()
    if opition.upper() == 'END':
        print('~' *40)
        print(f'{"See you later!":^40}')
        print('~' *40)
        break
    help(opition)
from time import sleep

color = (
    '\033[m',   # 0 reset
    '\033[42m', # 1 green
    '\033[44m', # 2 blue
    '\033[43m', # 3 yellow
    '\033[41m', # 4 red
    '\033[30;47m' # 5 white
)

def pyhelp(command, cor=0):
    title(f'Opening the documentation of the \'{command}\' command', cor=2)
    print(color[0], end='')
    sleep(0.5)
    print(color[5], end='')
    help(command)
    print(color[0], end='')

def title(msg, cor=0):
    print(color[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}')
    print('~' * (len(msg) + 4))
    print(color[0], end='')


while True:
    title('PyHELP System', 1)
    library = str(input('Function or library: ')).lower()
    if library == 'end':
        print('See you later!')
        break
    else:
        pyhelp(library)
