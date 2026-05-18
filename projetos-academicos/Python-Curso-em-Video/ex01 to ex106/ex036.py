valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
ano = int(input('Em quantos anos você quer pagar? '))
parcela = valor/(ano*12)
print('Cada parcela vai custar R${:.2f}' .format(parcela))

if parcela > sal/100 * 30:
    print('Não é possível financiar esta casa. O valor da parcela ultrapassa 30% do seu salário.')
else:
    print('É possível fazer o financiamento da casa.')