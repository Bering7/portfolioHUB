s = 0
for x in range(1,501,2):
    if x % 3 == 0:
        print(x)
        s += x
print('A soma de todos os números é {}' .format(s))