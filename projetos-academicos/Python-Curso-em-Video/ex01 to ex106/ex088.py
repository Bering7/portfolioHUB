import random
import time
mega = []
picks = []
n = int(input('How many bets do you want? '))
for c in range(0, n):
    while len(picks) < 6:
        x = random.randint(1,60)
        if x not in picks:
            picks.append(x)        
    picks.sort()
    mega.append(picks[:])
    picks.clear()
print(f'Drawing {n} bets')
for position, a in enumerate(mega):
    time.sleep(0.8)
    print(f'Bet {position+1}: {a}')
print('Good Lucky!')
