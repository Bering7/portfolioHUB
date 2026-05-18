lista = list()
while True:
    x = int(input('Digite um valor: '))
    if x in lista:
        print('Você ja digitou esse valor. Não vou adicionar novamente.')
    else:
        lista.append(x)
    escolha = str(input('Quer continuar? (S/N) '))
    while escolha not in 'SsNn':
        escolha = str(input('Não entendi sua resposta. Quer continuar? (S/N) '))
    if escolha in 'Nn':
        break
print(f'Você digitou os valores {sorted(lista)}')
