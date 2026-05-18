#isso aqui funciona sem a merda do loop while (e eu ainda fiz errado pq n funciona direito)
'''caixa = n50 = n20 = n10 = n1 = 0
while True:
    caixa = float(input('Qual valor você deseja sacar? R$'))
    n50 = caixa // 50
    n20 = n50 % 50 // 20
    n10 = n20 % 20 // 10
    n1 = n10 % 10 // 1
    print(f'Notas de R$50: {n50:.0f}')
    print(f'Notas de R$20: {n20:.0f}')
    print(f'Notas de R$10: {n10:.0f}')
    print(f'Notas de R$1: {n1:.0f}')
    break'''

#forma correta pq eu sou um animal
numero = int(input('Qual valor deseja sacar? R$'))
total = numero
cedula = 50
totcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Serão necessárias {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if total == 0:
            break
