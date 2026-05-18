n = int(input('Digite um número: '))
soma = maior = menor = n
m = 1
r = str(input('Quer continuar (S/N)? ')).strip()[0]
print('')
while r in 'Ss':
    n = int(input('Digite outro número: '))
    if n > maior:
            maior = n
    if n < menor:
            menor = n
    soma += n
    m += 1
    r = str(input('Você quer continuar (S/N)? ')).strip()[0]
    print('')
media = soma/m
print('A média dos números digitados é {:.2f}' .format(media))
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')
