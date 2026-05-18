import random
while True:
    n = int(input('Escolha um número: '))
    jogador = str(input('Par ou Ímpar? (P/I) '))[0]
    pc = random.randint(1, 10)
    pi = pc + n
    if pi % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {pc}. O total é {pi}: PAR.')
        if jogador in 'Pp':
            print('Você ganhou! \nJogue novamente...')
        elif jogador in 'Ii':
            print('Você perdeu. \nJogo encerrado.')
            break
    else:
        print(f'Você jogou {n} e o computador jogou {pc}. O total é {pi}: ÍMPAR.')
        if jogador in 'Ii':
            print('Você ganhou! \nJogue novamente...')
        elif jogador in 'Pp':
            print('Você perdeu. \nJogo encerrado.')
            break
