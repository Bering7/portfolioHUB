expressao = []
x = str(input('Digite a expressão: '))
pos = 0
while pos < len(x.strip()):
    expressao.append(x[pos])
    pos += 1
p_abertos = expressao.count('(')
p_fechados = expressao.count(')')
if p_abertos == p_fechados:
    print('A expressão é válida')
else:
    print('A expressão é inválida')
#esse código possui um bug

#codigo do guanabara sem bugs
expr = str(input('Digite a expressão: '))
x = []
for simb in expr:
    if simb == '(':
        x.append('(')
    elif simb ==')':
        if len(x) > 0:
            x.pop()
        else:
            x.append(')')
            break
if len(x) == 0:
    print('A expressão é válida')
else:
    print('A expressão é inválida')