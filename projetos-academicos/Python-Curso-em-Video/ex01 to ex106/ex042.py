a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro seguimento: '))

if a+b>c and a+c>b and b+c>a:
    print('É possível formar um triângulo com estes segmentos.')
    if a==b!=c or a==c!=b or b==c!=a:
        print('Classificação deste triângulo: isóceles.')
    elif a==b==c:
        print('Classificação deste triângulo: equilátero.')
    elif a!=b!=c:
        print('Classificação deste triângulo: escaleno.')
else:
    print('Não é possível formar um triângulo com estes segmentos.')