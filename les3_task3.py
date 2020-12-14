'''

3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

'''

def my_func(*args):
    args = list(args)
    args.sort(reverse=True)
    args.pop(len(args) - 1)
    result = args[0] + args[1]
    return result

number_1 = input('Enter first number.\n>>>')
number_2 = input('Enter second number.\n>>>')
number_3 = input('Enter third number.\n>>>')
if number_1.isdigit() and number_2.isdigit() and number_3.isdigit():
    number_1 = int(number_1)
    number_2 = int(number_2)
    number_3 = int(number_3)
else:
    print('You shoud enter an integers.')

result = my_func(number_1, number_2, number_3)
print(result)
print(type(result))

