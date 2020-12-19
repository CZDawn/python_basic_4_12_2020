'''

1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

'''

def division(arg1, arg2):
    '''Returns the quotient of division

    positional arguments:
    arg1 -- dividend (default - float)
    arg2 -- divider (default - float)

    (number, number) -> number

    >>> division(100.0, 5.0)
    20
    '''
    try:
        result = round(arg1 / arg2, 2)
    except ZeroDivisionError:
        result = 0
    return result


number1 = float(input('Enter dividend (example - 10.0):\n>>>'))
number2 = float(input('Enter divider (example - 5.0):\n>>>'))

print(f'The result of division is {division(number1, number2)}.')


assert division(10.0, 2.0) == 5.0
assert division(20, 10) == 2.0
assert division(20.3, 4.6) == 4.41

