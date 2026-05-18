import time
def bigger(*num):
    print('-' *30)
    print('Analizing the input values...')
    highest = 0
    for value in num:
        print(value, end=' ', flush=True)
        time.sleep(0.3)
        if value > highest:
            highest = value
    print(f'A total of {len(num)} value are reported.')
    print(f'The highest value reported was {highest}')
#Main program
bigger(7, 2, 9, 10, 1, 5, 8)
bigger(4, 8, 3)
bigger(6, 1)
bigger(8)
bigger()