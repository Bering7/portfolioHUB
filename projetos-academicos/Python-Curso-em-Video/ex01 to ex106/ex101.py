def vote(birth):
    import datetime
    year = datetime.date.today().year #importar uma biblioteca dentro da função economiza memória
    age = year - birth
    if age < 16:
       return f"Aged {age}, don't vote"
    elif age < 18 or age >= 70:
        return f"Aged {age}, optional vote"
    elif age >= 18:
        return f"Aged {age}, mandatory vote"
print(vote(int(input('Year of birth: '))))