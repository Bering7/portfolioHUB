dados = list()
dados.append('Pedro')
dados.append(25)

#pessoas = list()
#pessoas.append(dados[:]) #copia da lista dados, coloca a lista dados dentro da lista pessoas
#sem o [:] cria-se uma ligação entre as listas
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[0][0]) #vai mostrar o item 0 de pessoas[0] (Pedro)
print(pessoas[1][1]) #vai mostrar o item 1 de pessoas[1] (19)
print(pessoas[2][0]) #vai mostrar o item 0 de pessoas[2] (João)
print(pessoas[1])    #vai mostrar a lista 1 dentro da lista pessoas ['Maria', 19]
