#do meu jeito pq eu sou fresco
times = ('Flamengo', 'Cruzeiro', 'Bragantino', 'Palmeiras', 'Bahia', 'Fluminense', 'Atlético-MG', 
         'Botafogo', 'Mirassol', 'Corinthians', 'Grêmio', 'Ceará', 'Vasco', 'São Paulo', 'Santos',
         'Vitória', 'Internacional', 'Fortaleza', 'Juventude', 'Sport')
print('5 Primeiros:')
for posicao, time in enumerate(times[:5]):
    print(time)
print('-'*20)
print('4 Últimos:')
for posição, time in enumerate(times[15:]):
    print(time)
print('-'*20)
print('Em ordem alfabética: ', end='')
for c in sorted(times):
    print(c, end=', ')
print('')
print('-' *40)
print(f'O Vasco está na {times.index("Vasco")+1}° posição.') #usa-se .index para mostrar a posição do elemento na tupla
print('-'*20)

#do jeito do Guanabara
print(f'5 primeiros: {times[:5]}')
print('-'*60)
print(f'4 últimos: {times[16:]}')
print('-'*60)
print(f'Em ordem alfabética: {sorted(times)}')
print('-'*60)
print(f'O Vasco está na {times.index("Vasco")+1}° posição.')