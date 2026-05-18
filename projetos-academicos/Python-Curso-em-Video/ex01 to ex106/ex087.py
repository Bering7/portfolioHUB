matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
even = third_c = greater = 0
for line in range(0,3):
    for column in range(0,3):
        matrix[line][column] = int(input(f'Type an value to [{line}, {column}]: '))
        if matrix[line][column] % 2 == 0:
            even += matrix[line][column]
        if column == 2:
            third_c += matrix[line][column]
for value in matrix[1]:
    if value > greater:
        greater = value # == compara, = atribui
print('-' *25)
for line in matrix:
    for value in line:
        print(f'[{value:^5}]', end='')
    print()
print('-' *25)
print(f'The sum of the even values is: {even}')
print(f'The sum of the third column is: {third_c}')
print(f'The greater value in the second row is: {greater}') #row é melhor para ser utilizado no sentido de linha de uma matriz
