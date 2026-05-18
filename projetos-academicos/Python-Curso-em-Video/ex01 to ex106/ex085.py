'''odd = list() #ímpar
even = list() #par
for c in range(1,8):
    x = int(input(f'Type the {c}° value: '))
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
odd.sort()
even.sort()
print(f'the even numbers are: {even}')
print(f'the odd numbers are: {odd}')'''

#tem que fazer com uma lista dentro de outra
numbers = [[], []]
for c in range(1,8):
    x = int(input(f'Type the {c}° value: '))
    if x % 2 == 0:
        numbers[0].append(x)
        numbers[0].sort()
    else:
        numbers[1].append(x)
        numbers[1].sort()
print(f'The even numbers are: {numbers[0]}')
print(f'The odd numbers are: {numbers[1]}')