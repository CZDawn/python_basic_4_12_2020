'''

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

'''

import os

file_path = os.path.join(os.path.dirname(__file__), 'task_4.txt')
rus = ['Один', 'Два', 'Три', 'Четыре']

with open(file_path, 'r', encoding='UTF-8') as file:
    content = file.read().split()
    i = 0
    for el in rus:
        content[i] = el
        i += 3

with open('task4_new.txt', 'w', encoding='UTF-8') as file:
    i = 0
    while i < len(content):
        new_string = ''.join(content[i] + ' ' + content[i+1] + ' ' +  content[i+2])
        i += 3
        file.write(new_string + '\n')

