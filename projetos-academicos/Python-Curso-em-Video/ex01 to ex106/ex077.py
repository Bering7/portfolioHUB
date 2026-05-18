palavras = ('Lua',
            'Horizonte',
            'Brisa',
            'Relogio',
            'Fumaça',
            'Cacto',
            'Espelho',
            'Pedra',
            'Mare',
            'Farol',)
for c in palavras:
    print(f'\nNa palavra {c.upper()} temos: ', end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

#seria massa ter feito sozinho né henricão idiotao