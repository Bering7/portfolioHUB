n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1+n2)/2

print('A média para recuperação é de 5.0 a 6.9 pontos.')
print('A média mínima para aprovação é de 7.0 pontos.')

if media < 5:
    print(f'Sua média foi de {media} pontos.\nVocê está REPROVADO!')
elif 5 < media < 7:
    print(f'Sua média foi de {media} pontos.\nVocê está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi {media} pontos.\nParábens! Você está APROVADO!')