s = 0
for c in range(1,7):
    x = int(input('Escolha o {}° valor: ' .format(c)))
    if x % 2 == 0:
        s += x
print('A soma dos números pares digitados é {}' .format(s))