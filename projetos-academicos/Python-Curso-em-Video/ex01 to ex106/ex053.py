palavra = (input('Digite uma frase (desconsidere acentos): ')).strip()
print('A frase "{}" invertida fica "{}".' .format(palavra, palavra[::-1]))
for c in range(1):
    p = palavra.upper().split()
    pa = ''.join(p)
    inverter = pa[::-1]
    if pa == inverter:
        print('Temos um palíndromo')
    else:
        print('Não é um palíndromo')
print('')

#outra forma de fazer
string = (input('Digite uma frase: ')).strip().upper()
palavras = string.split()
junto = ''.join(palavras)
inverter = ''
for letter in range(len(junto)-1, -1, -1): #indo da última até a primeira letra
    inverter += junto[letter] #inverte a frase
print('A frase "{}" invertida é "{}".' .format(junto, inverter))
if junto == inverter:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')
    