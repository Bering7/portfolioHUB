p = float(input('Informe seu peso em Kg: '))
a = float(input('Informe sua altura em M: '))
imc = p/a**2
print('Seu IMC é de {:.2f}' .format(imc))

if imc < 18.5:
    print('Seu IMC está abaixo de 18,5. Você está abaixo do peso!')
elif imc < 25:
    print('Seu IMC está entre 18,5 e 25. Você com o peso normal.')
elif imc <= 30:
    print('Seu peso está entre 25 e 30; Você está com SOBREPESO!')
elif imc <= 40:
    print('Seu IMC está acima de 30. Você está com OBESIDADE!')
else:
    print('Seu IMC está acima de 40. Você está com OBESIDADE MÓRBIDA!')