'''n = 0
v = 0
c = 0
while n < 999:
    n = int(input('Digite um número (999 para parar): '))
    v += n
    c += 1
print('Você digitou {} números.' .format(c-1))
print('A soma deles é igual a {}' .format(v-999))'''

#tentando de outra forma, e de uma forma correta
n = s = c = 0
n = int(input('Digite um número (999 para parar): '))
while n < 999:
    s += n
    c += 1
    n = int(input('Digite um número (999 para parar): '))
print('Você digitou {} números e a soma deles é {}' .format(c, s))

'''a variável 'n' é usada antes do loop e no final dele para que a flag(999) n seja considerada'''
