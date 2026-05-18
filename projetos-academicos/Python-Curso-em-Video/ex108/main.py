import ex108.coin as coin
price = float(input('Type the price: '))
print(f'The half of {coin.coin(price)} is {coin.coin(coin.half(price))}')
print(f'The double of {coin.coin(price)} is {coin.coin(coin.double(price))}')
print(f'Increasing 10% of {coin.coin(price)} is {coin.coin(coin.increase(price))}')