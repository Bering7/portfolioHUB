# a = int(input('Digite um valor: ')) 
# b = int(input('Digite outro valor: '))
# c = int(input('Digite mais um valor: '))
# d = int(input('Digite o último valor: '))
# tupla = (a, b, c, d)
# é possivel tranformar automaticamente numa tupla da seguinte maneira
n = (int(input('Digite um valor: ')),
     int(input('Digite um valor: ')), 
     int(input('Digite um valor: ')), 
     int(input('Digite um valor: ')))
print(f'Você digitou os valores: {n}')
print(f'O número 9 aparece {n.count(9)} vezes.')
if 3 in n:
    print(f'O número 3 está na {n.index(3)+1}° posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os números pares digitados foram: ', end='')
for c in n: 
    if c % 2 == 0:
        print(c, end=' ')
