'''

6. Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'task_6.txt')

default_dict = {}

with open(file_path, 'r') as file:
    for line in file:
        temp_list = line.split(':')
        default_dict[temp_list[0]] = temp_list[1].split()

result_dict = {}
for key, value in default_dict.items():
    result_dict[key] = 0
    for el in value:
        try:
            result_dict[key] += int(el.split('(')[0])
        except ValueError:
            continue
print(result_dict)

