for par in range(0,51,2):
    print(par, end=' ') #o comando end faz ficar em apenas uma linha

#outra forma de fazer (mais idiota tambem)
for p in range(1,51):
    if p % 2 == 0:
        print(p, end=' ')