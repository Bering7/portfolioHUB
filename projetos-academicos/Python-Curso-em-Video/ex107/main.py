import moeda

price = float(input('Type the price: U$S'))
print(f'The half of U$S{price} is {moeda.half(price)}')
print(f'The double of U$S{price} is {moeda.double(price)}')
print(f'Increasing 10% of U$S{price} is {moeda.increase(price)}')