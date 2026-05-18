'''maior = 0
menor = 500
for c in range(1,6):
    peso = float(input('Qual o peso da {}° pessoa? '.format(c)))
    if peso > maior:
        maior=peso
    elif peso < menor:
        menor=peso
print('O maior peso informado foi {}' .format(maior))
print('O menor peso informado foi {}' .format(menor))
print('')'''

#do jeitin que o guanabara gosta, que eu achei até melhor
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Peso da {}° pessoa: ' .format(c)))
    if c == 1: #para o primeiro laço sendo executado
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso informado foi {}' .format(maior))
print('O menor peso informado foi {}' .format(menor))