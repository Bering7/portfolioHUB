lista = []
impares = []
pares = []
while True:
    lista.append(int(input('Digite um valor para a lista: ')))
    escolha = str(input('Quer continuar? (S/N) '))
    while escolha not in 'SsNn':
        escolha = str(input('Resposta inválida. Quer continuar? (S/N) '))
    if escolha in 'Nn':
        break
for valor in lista:
    if valor % 2 == 0:
        impares.append(valor)
    else:
        pares.append(valor)
print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')