'''

5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

'''

import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'task_5.txt')

numbers = [random.randint(1, 20) for el in range(1, 21)]

with open(file_path, 'w', encoding='UTF-8') as file:
    new_string = ' '.join(map(str, numbers))
    file.write(new_string)

with open(file_path, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))


