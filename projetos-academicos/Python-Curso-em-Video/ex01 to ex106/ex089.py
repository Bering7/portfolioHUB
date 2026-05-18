data = list()
while True:
    name = str(input('Name: '))
    g1 = float(input('Grade 1: '))
    g2 = float(input('Grade 2: '))
    avarege = (g1 + g2)/2
    data.append([name, [g1, g2], avarege])
    stay = str(input('Want to continue? [Y/N] '))
    if stay in 'Nn':
        break
print('-' *40)
print(f'{'No':<5}{'Name':<15}{'Avarege':>10}')
print('-' *40)
for i in range(0,len(data)):
    print(f'{i:<5}{data[i][0]:<15}{data[i][2]:>10}')
print('-' *40)
while True:
    n = int(input('Show the grades of wich student? (999 to stop) '))
    if n == 999:
        print('Program finished!')
        break
    else:
        print(f'The grades of {data[n][0]} are {data[n][1]}')
    print('-' *40)
