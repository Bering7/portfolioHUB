x = int(input('Você deseja a tabuada de qual número? '))
for y in range(1, 11):
    print('{} x {:2} = {:2}' .format(x, y, x*y))