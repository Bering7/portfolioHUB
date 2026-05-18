import datetime
data = dict()
year = datetime.date.today().year
data['name'] = str(input('Name: '))
birth = int(input('Year of birth: '))
data['age'] = year - birth
data['cpts'] = int(input('Work permit (0 if there is not): '))
if data['cpts'] != 0:
    data['year of hiring'] = int(input('Year of hiring: '))
    data['salary'] = int(input('Salary: R$'))
    data['retirement'] = (data['year of hiring'] + 35) - birth
print('-' *35)
for key, values in data.items():
    print(f'  -{key} has the value {values}')
