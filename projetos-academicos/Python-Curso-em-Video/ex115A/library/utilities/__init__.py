from colorama import init, Fore
init()

def leiaInt(msg):
    while True:
        try:
            value = int(input(msg))
        except:
            print('\033[31mERROR! Enter a valid integer.\033[m')
        else:
            return value

def line(tam=40):
    print('-' * tam)

def header(txt):
    line()
    print(txt.center(40))
    line()

def menu(lista):
    header('Main Menu')
    counter = 1
    for option in lista:
        print(f'{Fore.GREEN}{counter}\033[m - {Fore.BLUE}{option}\033[m')
        counter += 1
    line()
    option = leiaInt(Fore.GREEN + 'Your option: \033[m')
    return option

def porra(msg):
    return msg