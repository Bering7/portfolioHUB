#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = list()
menor = maior = 0
pmaior = list()
pmenor = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    for v in valores:
        if c == 1:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
for indice, v in enumerate(valores):
    if v == maior:
        pmaior.append(indice)
    if v == menor:
        pmenor.append(indice)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor da lista é o número {maior} nas posicões ', end='')
for c in pmaior:
    print(f'{c}... ', end='')
print(f'\nO menor número da lista é o número {menor} nas posicões ', end='')
for p in pmenor:
    print(f'{p}... ', end='')

#guanabara
'''print(f'Você digitou os valores: {valores}')
print(f'O maior valor da lista é o número {maior} nas posicões ', end='')
for indice, v in enumerate(valores):
    if v == maior:
        print(f'{indice}... ', end='')
print(f'\nO menor número da lista é o número {menor} nas posicões ', end='')
for indice, v in enumerate(valores):
    if v == menor:
        print(f'{indice}... ', end='')'''
