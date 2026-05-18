def leiaInt(msg):
    while True:
        value = input(msg)
        if value.isnumeric():
            break
        else:
            print('\033[31mERROR! Enter a valid integer.\033[m')
    return value

n = leiaInt('Type a number: ')
print(f'You just entered the number {n}.')
