data = dict()
goals = list()
data['name'] = str(input('Player name: '))
matches = int(input(f'How many matches {data["name"]} played? '))
for c in range(0, matches):
    goals.append(int(input(f'How many goals in match {c}? ')))
data['goals'] = goals
data['total'] = sum(goals)
print('-' *30)
print(data)
print('-' *30)
for key, value in data.items():
    print(f'The {key} field has the value {value}')
print('-' *30)
print(f'The player {data["name"]} has played {matches} matches.')
for index, value in enumerate(goals):
    print(f'    -In match {index}, did {value} goals.')
