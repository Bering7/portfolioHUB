import random
import time
import operator
data ={'player1': random.randint(1,6),
'player2': random.randint(1,6),
'player3': random.randint(1,6),
'player4': random.randint(1,6)}
print('Drawn Values:')
for key, value in data.items():
    time.sleep(0.6)
    print(f'{key} rolled {value} on the dice.')
ordered = dict(sorted(data.items(), key=operator.itemgetter(1), reverse=True)) #itemgetter serve para que o sorted use os números dentro do dicionario para organizar em ordem crescente
print('-------Players Ranking-------')
count = 1
for key, value in ordered.items():
    print(f'{count}° place: {key} with {value}')
    count += 1
