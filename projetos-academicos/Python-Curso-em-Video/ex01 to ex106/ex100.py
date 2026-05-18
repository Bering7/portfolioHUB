import random
def draws(lst):
    while len(lst) < 5:
        lst.append(random.randint(0, 100))
    print('The drawn values were:', end=' ')
    for value in lst:
        print(value, end=' ')
    print()
def sumEven(lst):
    even = 0
    for value in lst:
        if value % 2 == 0:
            even += value
    print(f'The sum of the even values is {even}')
#Main Program
numbers = list()
draws(numbers)
sumEven(numbers)