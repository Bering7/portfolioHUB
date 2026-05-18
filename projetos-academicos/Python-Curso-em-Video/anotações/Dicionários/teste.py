pessoas = {'nome': 'Henrique', 'sexo': 'M', 'idade': 18}
#pessoas['nome'] = 'Leandro'  #trocaria o nome Henrique para Leandro
pessoas['peso'] = 59.5 #adiciona o elemento para o dicionário pessoas
#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos') #em um print formatado as keys tem que estar em aspas duplas
for key, values in pessoas.items():
    print(f'{key} = {values}')

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'silga': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])'''

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #cria uma cópia do dicinário dentro da lista
for e in brasil: #laço para a lista
    for value in e.values():
        print(value, end=' ')
    print()
