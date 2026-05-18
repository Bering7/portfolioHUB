from math import factorial
from time import sleep
'''f = int(input('Digite um número para \ncalcular seu fatorial: '))
x = factorial(f)
print('Calculando...')
sleep(2)
print(f'{f}! = {f} ' ,end='')
while f-1 >= 1:
    print(f'x {f-1} ', end='')
    f -= 1
print(f'= {x}')'''

#dando uma mudadinha e facilitando a minha vida
a = int(input('Digite um número para \ncalcular seu fatorial: '))
c = a
f = factorial(a)
print(f'Calculando {a}! = ', end='')
sleep(2)
while c > 0:
    print('{}' .format(c), end='')
    print(' x ' if c>1 else (' = '), end='')
    c -= 1
print(f'{f}')