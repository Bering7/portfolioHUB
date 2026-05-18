#listas são feitas com colchetes[]
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
print(lanche)
#listas são mutáveis
lanche[3] = 'picolé' #muda o elemento pudim para picolé
print(lanche)

lanche.append('cookie') #o comando .append adiciona um elemento no final da lista
lanche.insert(0,'cachorro-quente') #adicona o cachorro quente antes de hamburguer

#métodos para apagar elementos
del lanche[3] #elimina o elemento 3(agora é a pizza)
lanche.pop(3) #pop é utilizado para eliminar o ultimo elemento, mas pode eliminar o elemento indicado
#lanche.remove('pizza') #nesse comando indica-se o conteúdo e não o índice
lanche.pop() #elimina o último elemento

'''ao tentar remover um elemento que não está na lista, o programara 
retornará um erro, mas é possível verificar se o elemento está na lista para
ter certeza'''
if 'pizza' in lanche:
    lanche.remove('pizza')

valores = list((range(4,11)))
'''fará uma contagem de 4 a 10 em ordem crescrente e transformará em uma lista'''

valor = list((range(0, 11)))
valor.sort() #deixará os valores da lista valor em ordem crescente
print(valor)
#valor.sort(reverse=True) #ordem descrescente
print(valor)
print(valor[::-3]) #fatiamento invertido para mostrar em ordem decrescente
len(valor) #mostra quantos itens tem na lista
