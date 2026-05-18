p = int(input('Digite um número inteiro: '))
if p <= 1:
    print('Não é primo.')
elif p == 2:
    print('É primo.')
elif p > 2 and p % 2 == 0:
    print('Não é primo')
else:
    for c in range(2, p):
        if p % c == 0:
            numero = 'Não é primo'
            break
        else:
            numero = 'É primo.'
    print(numero)
