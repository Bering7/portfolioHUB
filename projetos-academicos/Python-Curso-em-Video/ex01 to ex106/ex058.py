import random
x = random.randint(1, 100)
print('O computador escolheu um número entre 1 e 10, vamos chamá-lo de X. Tente adivinhar qual número foi escolhido.')
y = int(input('Seu chute: '))
tentativas = 1
while y != x:
    if x > y:
        y = int(input('X é maior que {}. Tente novamente: ' .format(y)))
        tentativas += 1
    elif x < y:
        y = int(input('X é menor que {}. Tente novamente: ' .format(y)))
        tentativas += 1
print('Você acertou em {} tentativas! O número correto é {}' .format(tentativas, x))