'''

2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя,
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

'''

class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

dividend = input('Enter a dividend:\n>>>')
divider = input('Enter a divider:\n>>>')

try:
    dividend = int(dividend)
    divider = int(divider)
    if divider == 0:
        raise DivisionByZero('Division by zero is not possible!')
except ValueError:
    print('You entered not an integer!')
except DivisionByZero as err:
    print(err)
else:
    print(f'Everything is good, result is - {dividend / divider}.')

