def leiaInt(msg):
    while True:
        try:
            value = int(input(msg))
        except:
            print('\033[31mERROR! Enter a valid integer.\033[m')
        else:
            return value

def leiaFloat(msg):
    while True:
        try:
            value = float(input(msg))
        except:
            print('\033[31mERROR! Enter a valid integer.\033[m')
        else:
            return value

n1 = leiaInt('Type a number: ')
n2 = leiaFloat('Type a real: ')
print(f'The integer value typed was {n1} and the real was {n2}')