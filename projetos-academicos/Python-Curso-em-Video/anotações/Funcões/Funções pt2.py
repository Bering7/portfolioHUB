#  Interactive Help
# help() usando no console
# help(print) #dentro do programa
print(input.__doc__)
help(input)

# Docstrings é basicamente uma string de uma documentação
import time
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    print(f'Couting from {i} to {f} by {p}')
    counting = i
    if counting <= f:
        print(f'{counting}', end='..')
        counting += p
    print('FIM!')

help(contador) #não ajuda em nada se não houver uma docstring dentro da função

#Parametros opcionais
def somar(a=0, b=0, c=0): #se c não receber nenhum valor, ele vale 0, sendo assim, um parâmetro opcional
    """
    Docstring for somar
    Faz a soma de 3 valores
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    """
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)

#Escopo de váriaves, escopo é o local onde a variável vai existir e tambem onde não vai existir
def teste():
    x = 8 #variável local
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

#Main program
n = 2 #varável global
print(f'No programa principal, n vale {n}')
teste() #'n' foi definido depois da função, mas tambem funciona dentro da função (escopo global)
# print(f'No programa principal, x vale {x}') #não funciona
#é possivel ter duas variaveis com o mesmo nome, desde que uma seja local e a outra seja global
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funcao()
print(f'N1 global vale {n1}')

#bagulho diferente
def funcao():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2 #n1 deixa de valer 2 e passa a valer 4 por causa do codigo 'global n1' e do valor atribuido em n1 dentro da função
funcao()
print(f'N1 global vale {n1}')

#RETORNO DE VALOREEEEESSSSSSSSSSSSS
#return
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma dos valores é {s}')

somar(3, 2, 5)
somar(2, 2)
somar(4)

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

# resposta = somar(3, 2, 5) #dentro de uma variavel
# print(somar(3, 2, 5))
r1 = somar(3, 2, 5)
r2 = somar(1, 7)
r3 = somar(4)
print(f'Meus cálculos deram {r1}, {r2}, {r3}')