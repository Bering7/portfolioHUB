matrix = [[], [], []]
for x in range(0,3):
    for c in range(0,3):
        matrix[x].append(int(input(f'Type an value to [{x}, {c}]: ')))
for line in matrix:
    for value in line:
        print(f'[{value:^5}]', end='') #:^5 faz com que tenha 5 espaços e que o valor fique centralizado dentro dos colchetes
    print()