import datetime
ano = int(input('Ano de nascimento: '))
a = datetime.datetime.now().year
i = a - ano

print('Você tem {} anos.' .format(i))

if i <= 9:
    print('Categoria: MIRIM.')
elif i <= 14:
    print('Categoria: INFANTIL.')
elif i <= 19:
    print('Categoria: JUNIOR.')
elif i == 20:
    print('Categoria: SÊNIOR.')
else:
    print('Categoria: MASTER.')