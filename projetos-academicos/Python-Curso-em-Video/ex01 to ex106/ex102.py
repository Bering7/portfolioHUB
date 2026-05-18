def factorial(n, show=False):
    """
    Docstring for factorial
    Calculate the factorial of a number n
    :param n: The number to be calculated
    :param show: (optional) Show the calculation or not
    return: The factorial value of a number n
    """
    from math import factorial
    f = factorial(n)
    if show==True:
        while n > 0:
            print(n, end='')
            print(' x ' if n>1 else (' = '), end='')
            n -= 1
        return f
    else:
        return f
    
print(factorial(10, False))
# help(factorial)