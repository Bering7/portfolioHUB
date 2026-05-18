def increase(price):
    i = price + (price * 10/100)
    return i

def decrease(price):
    d = price - (price * 10 / 100)
    return d

def double(price):
    doub = price * 2
    return doub

def half(price = 0):
    hal = price // 2
    return hal

def coin(price = 0, coin = 'R$'):
    return f"{coin}{price:.2f}".replace('.', ',')