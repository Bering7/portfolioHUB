#tabuada com loop while e break
#uma forma mais simples q eu simplesmente esqueci

while True:
    n =  int(input('Quer ver a tabuada de qual valor? '))
    print('-' *15)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 15)