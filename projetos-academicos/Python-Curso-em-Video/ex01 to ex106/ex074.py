#do meu jeitinho burro (talvez nao tao burro)
import random
numeros = tuple(random.sample(range(0, 10), k=5))
print(f'Os números gerados foram:')
maior = 0
menor = random.choice(numeros)
for c in numeros:
    print(c, end=', ')
    if c > maior:
        maior = c
    if menor > c:
        menor = c
print('')
print(f'''O maior número gerado foi: {maior}
O menor número gerado foi: {menor}''')
print('')

#jeitinho guanabara (po achei mt melhor)
n = (random.randint(1,10), random.randint(1,10), random.randint(1,10),
     random.randint(1,10), random.randint(1,10),)
print('Os números sorteados foram: ', end='')
for c in n:
    print(c, end=' ')
print(f'\nO maior número sorteado foi: {max(n)}') #o max() mostra o maior valor de uma tupla, facilitando o jeito de mostrar o maior valor
print(f'O menor número sorteado foi: {min(n)}') #o min() mostra o maior valor de uma tupla, facilitando o jeito de mostrar o maior valor
