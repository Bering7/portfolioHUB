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