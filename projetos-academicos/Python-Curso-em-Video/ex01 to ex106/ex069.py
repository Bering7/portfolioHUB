n = c = s = homem = mulher = 0
while True:
    n = int(input('Qual a idade da pessoa? '))
    s = ' '
    while s not in 'HhMm':
        s = str(input('Homem ou Mulher? (H/M) '))[0]
    if n >= 18:
        c += 1
    if s in 'Hh':
        homem += 1
    if n < 20 and s in 'Mm':
        mulher += 1
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? (S/N) '))[0]
    print('-' *25)
    if continuar in 'Nn':
        break
print(f'''Maiores de 18: {c} 
Homens: {homem}
Mulheres com menos de 20: {mulher}''')
print('-' *25)