print('-' *22)
print('10 TERMOS DE UMA P.A!')
print('-' *22)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(10):
    an = a1 + c*r
    print(an, end=' ')
print('acabou')

#outra forma de fazer
print(' ')

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
a10 = a1 + (10-1) * r #cálculo de um termo n da P.A (nesse caso, o décimo termo)

for c in range(a1, a10+1, r):
    print(c, end=' ')
print('acabou de novo')