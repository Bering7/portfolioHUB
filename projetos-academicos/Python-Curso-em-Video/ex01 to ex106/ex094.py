person = dict()
all = list()
total = 0
while True:
    person['name'] = str(input('Name: '))
    person['sex'] = str(input('Sex: (M/F) ')).upper()
    while person['sex'] not in 'MF':
        print('Invalid response! Please enter only M or F.')
        person['sex'] = str(input('Sex: (M/F) ')).upper()
    person['age'] = int(input('Age: '))
    total += person['age']
    all.append(person.copy())
    person.clear()
    option = str(input('Continue? (S/N) '))
    while option not in 'SsNn':
        print('Invalid responde! Please enter only S or N.')
        option = str(input('Contiue? (S/N) '))
    if option in 'Nn':
        break
avarege = total/len(all)
print('-' *45)
print(f'A) In total we have {len(all)} registered people.')
print(f'B) The age avarege is {avarege:.2f} years.')
print('C) The registered womans was', end=' ')
for w in all:
    if w['sex'] in 'Ff':
        print(f'{w["name"]}', end=' ')
print()
print('D) List of peoples who are above avarege:')
for c in all:
    if c['age'] >= avarege:
        for key, value in c.items():
            print(f'    {key} = {value};', end=' ')
        print()
print('Finished')
