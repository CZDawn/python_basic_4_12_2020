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
from functools import reduce

file_path = os.path.join(os.path.dirname(__file__), 'task_7.txt')

def make_dict(some_list, iter_count, data_position):
    new_list = []
    i = 0
    while i < len(some_list):
        if some_list[i+data_position].isdigit():
            new_list.append(int(''.join(some_list[i+data_position])))
        else:
            new_list.append(''.join(some_list[i+data_position]))
        i += iter_count
    return new_list

with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.read().split()
    firm_name_list = make_dict(content, 4, 0)
    proceeds_list = make_dict(content, 4, 2)
    costs_list = make_dict(content, 4, 3)
    profits_list = []
    financial_result = []
    i = 0
    while i < len(proceeds_list):
        result = proceeds_list[i] - costs_list[i]
        if result > 0:
            profits_list.append(result)
            financial_result.append(result)
        else:
            financial_result.append(result)
        i += 1
    average_profit = {'average_profit': round(sum(profits_list) / len(profits_list), 2)}
    fin_result_dict = dict(zip(firm_name_list, financial_result))
    result_list = [fin_result_dict, average_profit]

with open('task_7_result.json', 'w', encoding='UTF-8') as file:
    json.dump(result_list, file)

