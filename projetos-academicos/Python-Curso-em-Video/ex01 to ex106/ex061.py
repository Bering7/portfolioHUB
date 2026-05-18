a1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão: '))
a10 = a1 + (10-1) * r #cálculo de um termo n da P.A (nesse caso, o décimo termo)
while a1 < a10+1:
    print(f'{a1}', end=' ')
    a1 += r
print('Acabou.')

#uma forma de fazer sem calcular o décimo termo
a1 = int(input('Primeiro termo da P.A: '))
r = int(input('Razão: '))
termo = a1
c = 1
while c <= 10:
    print('{} '.format(a1), end='')
    termo += r
    c += 1
print('Acabou')