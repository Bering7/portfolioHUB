# <7 REC <5 REPROVADO
data = dict()
data['name'] = str(input('Name: '))
data['avarege'] = float(input('Avarege: '))
if data['avarege'] < 5:
    data['status'] = 'Did not pass'
elif data['avarege'] < 7:
    data['status'] = 'Recovery'
else:
    data['status'] = 'Passed'
print('-' *20)
for key, value in data.items():
    print(f'{key} is {value}')
