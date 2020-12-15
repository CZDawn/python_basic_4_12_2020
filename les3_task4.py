'''

4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

'''

def my_func(x, y):
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if y < 0:
            return (x ** -(y))
        elif y > 0:
            return x ** y
        else:
            return 1
    else:
        print('You shoud enter an integers.')

variable_x = input('Enter a positive number:\n>>>')
variable_y = input('Enter a negative number:\n>>>')

result = my_func(variable_x, variable_y)
print(result)

