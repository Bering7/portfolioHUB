import time
def line():
    print('-'*30)
def tocount(start, final, step):
    print(f'Couting from {start} to {final} by {step}')

    counting = start
    if step < 0:
        step *= -1
    if step == 0:
        step = 1
    if counting < final:
        while counting <= final:
            print(counting, end=' ', flush=True) #flush nao deixar o programa ligar o buffer de tela
            time.sleep(0.5)
            counting += step
        print('END!')
    else:
        while counting >= final:
            print(counting, end=' ', flush=True)
            time.sleep(0.5)
            counting -= step
        print('END!')
tocount(1, 10, 1)
line()
tocount(10, 0, 2)
line()
print(f'{"It's yout turn to costumize de counting!"}')
s = int(input('Start: '))
f = int(input('End: '))
st = int(input('Step: '))
line()
tocount(s, f, st)
