v = float(input('Qual o valor do produto? R$'))
print('')
print('Formas de pagamanto: ')
print('[1] À vista no dinheiro/cheque. (10% de desconto)')
print('[2] À vista no cartão. (5% de desconto)')
print('[3] 2x no cartão (Preço normal)')
print('[4] 3x ou mais (20% de juros)')
print('')
p = int(input('Digite o número corresponde à forma de pagamento que você utilizará: '))

if p == 1:
    print('O valor de R${:.2f} passará a ser de R${:.2f}' .format(v, v - v/100*10))
elif p == 2:
    print('A forma de pagamento selecionada foi: À vista no cartão.')
    print('Será aplicado 5% de desconto. O preço a ser pago passará a ser de: R${:.2f}' .format(v - v/100*5))
elif p == 3:
    print('A sua compra será parcelada em 2x de R${:.2f}.' .format(v/2))
elif p == 4:
    x = int(input('Em quantas parcelas? '))
    n = v + v/100 * 20
    print(f'Seu produto será parcelado em {x}x de R${n/x:.2f} com juros.')
    print(f'O produto de R${v:.2f} passará a custar R${n:.2f}')
else:
    print('Essa opção não existe.')