s = 0
mulheres = 0
homem_idade = 0
homem_nome = ''
for c in range(1, 5):
    print('-' *20)
    nome = (input('Nome da {}° pessoa: ' .format(c))).strip().upper()
    idade = int(input('Idade: ' .format(c)))
    sexo = input('Sexo: ' .format(c)).strip().upper()
    print('-' *20)
    s += idade
    if idade < 20 and sexo == 'FEMININO':
        mulheres += 1
    elif idade > homem_idade and sexo == 'MASCULINO':
        homem_idade = idade
        homem_nome = nome
media = s/4
print('A média de idade do grupo é {}.' .format(media))
print('O homem mais velho se chama {}.' .format(homem_nome.capitalize()))
print('{} mulheres do grupo tem menos de 20 anos.' .format(mulheres))
