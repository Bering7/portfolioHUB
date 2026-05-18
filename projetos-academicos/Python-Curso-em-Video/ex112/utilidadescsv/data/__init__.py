def readMoney(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'ERROR: "{entrada}" is a invalid price.')
        else:
            valido = True
            return float(entrada)