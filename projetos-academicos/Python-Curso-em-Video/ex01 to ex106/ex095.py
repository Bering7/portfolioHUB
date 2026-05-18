player = dict()
goals = list()
team = list()
while True:
    player['name'] = str(input('Player name: ')).strip()
    matches = int(input(f'How many matches {player["name"]} played? '))
    for c in range(0, matches):
        goals.append(int(input(f'How many goals in match {c+1}? ')))
    player['goals'] = goals[:]
    player['total'] = sum(goals)
    team.append(player.copy())
    player.clear()
    goals.clear()
    while True:
        option = str(input('Continue? ')).upper()[0]
        if option in 'SN':
            break
        print('Invalid responde! Please enter only S or N.')
    if option == 'N':
        break
print('='*40)
print(f'{'cod':<5}{'name':<15}{'goals':<10}{'total':>10}')
print('-'*40)
for key, value in enumerate(team):
    print(f'{key:<5}', end='')
    for data in value.values():
        print(f'{str(data):<15}', end='')
    print()
print('='*40)
while True:
    option = int(input('Show data for wich player? (999 to stop) '))
    if option == 999:
        print('Finished')
        break
    if option >= len(team):
        print(f'Invalid responde! There is no player with code {option}')
    else:
        print(f'-- Player data for {team[option]["name"]}:')
        for i, value in enumerate(team[option]['goals']):
            print(f'    In match {i+1} did {value} goals.')
    print('-'*40)
