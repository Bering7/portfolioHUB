#dolar = 3.27 reais
real = float(input('Quanto você tem na carteira? R$'))
dolar = real/5.47
euro = real/6.38
print(f'Você pode comprar USD${dolar:.2f} ou €{euro:.2f}')