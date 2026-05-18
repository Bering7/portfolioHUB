#Estrutura semelhante a tuplas e listas, mas agora podemos ter índices literais (personalizar os índices)
# Dincionarios sao identificados com {}
#dados = dict() #ou dados = {}
dados = {'nome':'Pedro', 'idade':25}
print(dados['nome']) #Pedro
print(dados['idade']) #25
dados['sexo'] = 'M' #adicionará o indice 'sexo' no dicionario dados
del dados['idade'] #eliminará o 25 deixando o dicionário apenas com Nome e Sexo

filme = {'titulo':'Star Wars',
        'ano':1977,
        'diretor':'George Lucas'
        }
print(filme.values()) #mostrá os valores dentro do dicionário
print(filme.keys()) #mostrará as chaves (titulo, ano...)
print(filme.items()) #mostrará os valores e as chaves

#utilizando em laços
for key, value in filme.items():
    print(f'O {key} é {value}') #O título é Star Wars

#dicionário dentro de uma lista
locadora = [{'titulo':'Star Wars', 'ano':1977, 'diretor':'George Lucas'},
            {'titulo':'Avenger', 'ano':2012, 'diretor':'Joss Wheadon'},
            {'titulo':'Matrix', 'ano':1999, 'diretor':'Wachowski'}]
print(locadora[0]['ano']) #1977
print(locadora[2]['titulo']) #Matrix
