'''

1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

'''

def division(arg1, arg2):
    try:
        result = arg1 / arg2
    except ZeroDivisionError:
        result = 0
    return result

number1 = input('Enter dividend:\n>>>')
number2 = input('Enter divider:\n>>>')
if number1.isdigit()  and number2.isdigit():
    number1 = int(number1)
    number2 = int(number2)
else:
    print('You shoud enter an integer')

result = division(number1, number2)

print(f'The result of division is {result}.')

