def coin(price = 0, coin = 'R$'):
    return f'{coin}{price:.2f}'.replace('.', ',')

def increase(price=0, rate=0, formatting = True):
    increase = price + (price * rate/100)
    if formatting:
        increase = coin(increase)
    return increase

def double(price = 0, formatting = True):
    double = price * 2
    if formatting:
        double = coin(double)
    return double

def half(price = 0, formatting = True):
    half = price / 2
    return coin(half) if formatting else half

def decrease(price = 0, rate = 0, formatting = True):
    decrease = price - (price * rate/100)
    return coin(decrease) if formatting else decrease

def overview(price = 0, rateincrease = 0, ratedecrease = 0):
    print('-' *40)
    print('Overview'.center(40))
    print('-' *40)
    print(f'Analyzed price: \t{coin(price)}')
    print(f'Double of the price: \t{double(price)}')
    print(f'Half of the price: \t{half(price)}')
    print(f'{rateincrease}% increase: \t\t{increase(price, rateincrease)}')
    print(f'{ratedecrease}% decrease: \t\t{decrease(price, ratedecrease)}') # \t para tabulação
    print('-' *40)
