import datetime
atual = datetime.datetime.now().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? ' .format(c)))
    idade = atual - nasc
    if idade < 18:
        menor += 1
    else:
        maior += 1
print('{} pessoas já alcançaram a maioridade.' .format(maior))
print('{} ainda estão na menorida.' .format(menor))