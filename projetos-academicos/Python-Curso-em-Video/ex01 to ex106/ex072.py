numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Trêze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
print(numeros[15])
a = int(input('Digite um número de 0 a 20: '))
while a < 0 or a > 20:
    a = int(input('Tente novamente. Digite um número de 0 a 20: '))
print(f'Você digitou o número {numeros[a]}')