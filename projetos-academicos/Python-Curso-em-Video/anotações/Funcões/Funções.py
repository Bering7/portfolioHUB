def mostraLinha():
    print('-'*30)
mostraLinha()
print('       Sistema De Alunos          ')
mostraLinha()

def mensagem(msg): #mensagem recebe msg, posso colocar o que eu quiser no lugar de msg
    print('-'*30)
    print(msg)
    print('-'*30)
mensagem('     SITEMA DE ALUNOS     ') #msg passa a ser 'SISTEMA DE ALUNOS
mensagem('     PYTHON É CHAVE     ')

a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)


def som(a, b):
    s = a + b
    print(s)


#Prgorama principal
som(a=4, b=5)
som(8, 9)
som(2, 1)
#soma(4) da erro pois soma precisa receber 2 parâmetros

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')
soma(a=4, b=5)
soma(b=4, a=5)

def contador(*num): #o asterisco servem para o programa entender que o usuario colocará diversios numeros(desempacotamento)
    print(num)
    for valor in num:
        print(valor, end=' ')
    print('Fim!')
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst): #lst tambem vira uma lista depois
    pos = 0
    while pos < len(lst):
        lst[pos]*=2
        pos += 1
valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)