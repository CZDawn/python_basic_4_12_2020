'''

1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

'''
from sys import argv

script_name, first_param, second_param, third_param = argv

def salary(first_param, second_param, third_param):
    '''Return total salary with prize

    positional arguments:
    first_param -- quantity of hours of your work (default - float)
    second_param -- rate per hour of your work (default - float)
    third_param -- percentage of prize for your work (default - float)

    (number, number, number) -> number

    >>> salary(40.0, 1000.0, 20.0)
    48000
    '''
    first_param = float(first_param)
    second_param = float(second_param)
    third_param = float(third_param)

    sum_salary = first_param * second_param
    prize = sum_salary * third_param / 100
    total = sum_salary + prize
    return total

print(salary(first_param, second_param, third_param))

