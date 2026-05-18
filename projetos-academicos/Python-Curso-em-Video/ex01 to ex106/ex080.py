lista = []
for cont in range(0, 5):
    x = int(input('Digite um valor: '))
    if cont == 0 or x > lista[-1]: #se for a primeira ocorrencia ou X for maior que o último número
        lista.append(x)
        print('O valor foi adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if x < lista[pos]:
                lista.insert(pos, x)
                print(f'Número adicionado na posição {pos}')
                break
            pos += 1
print(f'Os números digitados em ordem foram: {lista}')
