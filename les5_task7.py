'''

7. Создать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
а также среднюю прибыль.

Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.

Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка:
[{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.

'''

import os
import json

file_path = os.path.join(os.path.dirname(__file__), 'task_7.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.read().split()
    proceeds_list = []
    costs_list = []
    profits_list = []
    i = 0
    while i < len(content):
        proceeds_list.append(int(''.join(content[i+2])))
        costs_list.append(int(''.join(content[i+3])))
        i += 4
    j = 0
    while j < len(proceeds_list):
        profits_list.append(proceeds_list[j] - costs_list[j])
        j += 1 

print(content)
print(proceeds_list)
print(costs_list)
print(profits_list)

