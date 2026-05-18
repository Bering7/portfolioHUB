numero = int(input('Informe um número: '))
m = numero // 1000 % 10
c = numero // 100 % 10
d = numero // 10 % 10
u = numero // 1 % 10
print(f'''milhar: {m}
centena: {c}
dezena: {d}
unidade: {u}''')