#lanche = 'hamburguer'
#lanche = 'suco'
#será atribuido apenas a variavel suco, não é possivel as duas

'''para fazer isso ser possível, se utiliza as tuplas, listas ou dicionarios, mas estou
mas estou utilizando apenas tuplas'''

#usando o loop for
#lanche = ('Hamburber', 'Suco', 'Pizza', 'Pudim')
#for c in lanche:
#    print(c) #ele mostra na tela todos os elementos da variavel lanche

'''truplas são imutaveis, isso quer dizer que não se pode mudar a tupla enquanto o programa
está sendo executado'''

lanche = ('Hamburber', 'Suco', 'Pizza', 'Pudim') #tuplas são declaradas com ou sem parenteses

#fatiamento
print(lanche) #mostra toda a tupla
print(lanche[1]) #mostra o segundo elemento da tupla
print(lanche[-2]) #mostra o terceiro elemento da tupla
print(lanche[1:3]) #mostra do segundo ao terceiro elemento da tupla
print(lanche[2:]) #mostra do segundo ao ultimo elemento da tupla
print(lanche[:2]) #mostra do primeiro ao segundo elemento da tupla
print(lanche[-2:]) #mostra do terceiro elemento ao final da tupla

#truplas são imutáveis
#lanche[1] = refrigerante #retornará uma mensagem de erro

#para não mostrar a tupla com os parenteses e as aspas
for comida in lanche:
    print(f'Eu vou comer {comida}')
#ou
for contador in range(0, len(lanche)):
    print(lanche[contador]) #com esse é possivel mostrar a posição dos elementos
#mais uma forma de mostrar o elemnto e sua posicao
for posicao, comidas in enumerate(lanche):
    print(f'Eu vou comer {comidas} na posição {posicao}')


print(sorted(lanche)) #mostra em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) #mostra a tupla a junto com a tupla b, e a ordem tem influencia
print(len(c)) #mostra quantos elementos tem na tupla
print(c.count(5)) #mostra quantas vezes o numero 5 aparece em c
print(c.index(8)) #mostra em que posição está o número 8


pessoa = ('Henrique', 17, 'Masculino', 61.50)
#del(pessoa) #apaga uma variável, e não pode deletar um único item
import random
fodase = tuple(random.sample((range(0,11))))
print(fodase)