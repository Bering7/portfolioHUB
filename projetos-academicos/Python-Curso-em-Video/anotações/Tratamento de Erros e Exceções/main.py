'''try:
    operação
   except:
    falhou

pode se ter mais excepts

   else:
    deu certo
   finally: # ocorre independente de falha ou sucesso
'''

'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema.')
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')'''


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')