lista = ('Banana', 0.99, 
        'Maçã', 1.99,  
        'Uva', 3.50, 
        'Mamão', 2, 
        'Melancia', 3, 
        'Abacaxi', 7)
#pode ser feito verificando a posição dos produtos (ímpar) e seus preços (pares)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:<9}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')