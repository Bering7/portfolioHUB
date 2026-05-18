def ficha(n='Unknown', g=0):
    print(f'The player {n} scored {g} goals in the championship.')

name = str(input('Player name: '))
goals = str(input('Number of goals: '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
if name.strip() == '':
    ficha(g=goals)
else:
    ficha(name, goals)
