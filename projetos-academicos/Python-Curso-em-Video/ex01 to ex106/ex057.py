sexo = ''
while sexo in '':
    sexo = str(input('Qual o seu sexo (M/F)? ')).strip()[0] #o programa considerará apenas a primeira letra, o usuario pode digitar o sexo inteiro
    if sexo in 'MmFf':
        if sexo in 'Mm':
            print('O sexo selecionado foi masculino.')
        elif sexo in 'Ff':
            print('O sexo selecionado foi feminino.')
    else:
        sexo = ''
        print('Resposta inválida. Tente novamente.')

#forma mais simples de ser feita
sexo = str(input('Qual o seu sexo (M/F)? ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Resposta inválida. Por favor, informe seu sexo: ')).strip().upper()[0]
print('O sexo informado foi {}.'.format(sexo))
