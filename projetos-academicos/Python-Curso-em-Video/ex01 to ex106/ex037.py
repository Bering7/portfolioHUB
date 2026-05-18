num = int(input('Enter an integer number: '))
bin = bin(num)
oct = oct(num)
hex = hex(num)
print('''[ 1 ] Binary
[ 2 ] Octal
[ 3 ] Hexadecimal''')
selection = int(input('Select an option: '))
if selection == 1:
    print(f'The number {num} in Binary is: {bin[2:]}')
if selection == 2:
    print(f'The number {num} in octal is: {oct[2:]}')
if selection == 3:
    print(f'The number {num} in hexadecimal is: {hex[2:]}')
