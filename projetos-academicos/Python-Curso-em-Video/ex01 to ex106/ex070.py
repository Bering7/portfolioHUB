total = menor = caros = 0
barato = ' '
while True:
    print('-' *30)
    nome = str(input('Qual o nome do produto? ')).strip().capitalize()
    preço = float(input('Qual o valor do produto? R$'))
    print('-' *30)
    total += preço
    if preço > 1000:
        caros += 1
    if menor < preço:
        menor == preço
        barato = nome
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? (S/N)'))[0]
    if continuar in 'Nn':
        break
print('-' *30)
print(f'''O total da compra é: R${total:.2f}
{caros} produtos custam mais de R$1000,00.
O produto mais barato é: {barato}''')
