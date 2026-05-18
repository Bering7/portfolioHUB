'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)'''

valores = list()
for contador in range(0, 5):
    valores.append(int(input('Digite um número: ')))
    
for c, v in enumerate(valores):
    print(f'Na posição {c} achei o número {v}!')

a = [2, 3, 4, 7]
# b = a (cria uma ligação entre a lista a e b)
b = a[:] #com o fatiamento podemos criar uma cópia da lista a
b[2] = 8
print(f'Lista a: {a}')
print(f'Lista b: {b}')