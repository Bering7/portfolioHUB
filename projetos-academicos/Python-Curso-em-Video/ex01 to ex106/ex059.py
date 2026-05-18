a = float(input('Digite o 1° valor: '))
b = float(input('Digite o 2° valor: '))
escolha = 0
while escolha != 5:
    print('-------OPÇÕES-------')
    print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa') #pode ser ultilizada 3 aspas para escrever em mais de 1 linha
    escolha = int(input('Escolha uma opção: '))
    if escolha == 1:
        print('A soma dos números {} e {} é igual a {}.' .format(a, b, a+b))
    elif escolha == 2:
        print('O produtos dos números {} e {} é igual a {}.' .format(a, b, a*b))
    elif escolha == 3:
        if a > b:
            maior = a
        else:
            maior = b
        print('O maior número digitado foi {}' .format(maior))
    elif escolha == 4:
        a = float(input('Digite o 1° valor novamente: '))
        b = float(input('Digite o 2° valor novamente: '))
    elif escolha == 5:
        print('Programa encerrado.')
    else:
        print('Opção inválida. Tente novamente.')
