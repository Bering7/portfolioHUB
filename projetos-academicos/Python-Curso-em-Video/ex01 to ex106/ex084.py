pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? (S/N) '))
    if resposta in 'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
maior = menor = 0
pesada = list()
leve = list()
for cont in range(0, len(pessoas)):
    if cont == 0:
        maior = menor = pessoas[cont][1]
    else:
        if pessoas[cont][1] > maior:
            maior = pessoas[cont][1]
        if pessoas[cont][1] < menor:
            menor = pessoas[cont][1]
for cont in range(0, len(pessoas)):
    if menor == pessoas[cont][1]:
        leve.append(pessoas[cont][0])
    if maior == pessoas[cont][1]:
        pesada.append(pessoas[cont][0])
print(f'O maior peso foi de {maior}Kg. Peso de {pesada}')
print(f'O menor peso foi de {menor}Kg. Peso de {leve}')
