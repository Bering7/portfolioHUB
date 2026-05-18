import coin
money = float(input('Type the price: '))
print(f'The half of {coin.coin(money)} is {coin.half(money, True)}')
print(f'The double of {coin.coin(money)} is {coin.double(money, False)}')
print(f'Increasing 10% of {coin.coin(money)} is {coin.increase(money, 10, True)}')