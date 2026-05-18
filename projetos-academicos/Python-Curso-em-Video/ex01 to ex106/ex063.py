'''termos = int(input('Quantos termos quer mostrar? '))
a, b = 0, 1
c = 1 #o contador deve ser igual a 1 para mostrar os termos informados pelo usuário
while c <= termos:
    print(a, end=' ')
    a, b = b, a + b
    c += 1'''

#do jeitão guanabara que todo mundo gosta
termos = int(input('Quantos termos quer mostrar? '))
a = 0
b = 1
print('{} {} '.format(a, b), end='')
cont = 1
while cont <= termos:
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    cont += 1