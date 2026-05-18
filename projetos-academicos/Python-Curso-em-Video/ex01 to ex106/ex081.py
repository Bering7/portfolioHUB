lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Quer continuar? (S/N)'))
    while escolha not in 'SsNn':
        escolha = str(input('Resposta inválida. Quer continuar? (S/N)'))
    if escolha in 'Nn':
        break
#quantos números foram digitados
print(f'Você digitou {len(lista)} valores para a lista.')
#ordenada de forma decrescente
lista.sort(reverse=True)
print(f'A lista em ordem descrescente é: {lista}')
#se o valor 5 está ou não na lista
if 5 in lista:
    print(f'O número 5 está na lista!')
else:
    print('O número 5 não está na lista.')
