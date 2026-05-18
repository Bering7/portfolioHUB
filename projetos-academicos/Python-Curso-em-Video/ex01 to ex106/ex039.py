import datetime
nasc = int(input('Informe o ano que você nasceu: '))
ano = datetime.datetime.now().year
i = ano - nasc

if i > 18:
    print('Você já tem {} anos, deveria ter se alistado há {} anos, em {}.' .format(i, i-18, ano-(i-18)))
elif i < 18:
    print('Você ainda tem {} anos, deve se alistar em {} anos, em {}.' .format(i, 18-i, ano+(18-i)))