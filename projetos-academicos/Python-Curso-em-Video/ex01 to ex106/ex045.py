import colorama
import random
import time
colorama.init()
comp = ['PEDRA', 'PAPEL', 'TESOURA']
x = random.randint(0, 1)
print('Suas opções:')
print('[0] PEDRA \n[1] PAPEL \n[2] TESOURA')
a = int(input('Escolha sua jogada: '))
print('')
print('JO'), time.sleep(1), print('KEN'), time.sleep(1), print('PO!'), time.sleep(0.4)
print('')
print('O computador escolheu: {}' .format(comp[x]))
print('O jogador escolheu: {}' .format(comp[a]))
print('')
if x == 0: #pedra
    if a == 0:
        print(colorama.Fore.BLUE+'EMPATE!')
    elif a == 1:
        print(colorama.Fore.GREEN+'O jogador VENCEU!')
    elif a == 2:
        print(colorama.Fore.RED+'O conputador VENCEU!')
elif x == 1: #papel
    if a == 0:
        print(colorama.Fore.RED+'O computador VENCEU!')
    elif a == 1:
        print(colorama.Fore.BLUE+'EMPATE!')
    elif a == 2:
        print(colorama.Fore.GREEN+'O jogador VENCEU')
elif x == 2: #tesoura
    if a == 0:
        print(colorama.Fore.GREEN+'O jogador VENCEU!')
    elif a == 1:
        print(colorama.Fore.RED+'O computador VENCEU!')
    elif a == 2:
        print(colorama.Fore.BLUE+'EMPATE!')