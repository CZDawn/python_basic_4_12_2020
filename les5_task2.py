'''

2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

'''
from typing import List
import os

file_path = os.path.join(os.path.dirname(__file__), 'task_2.txt')

def get_counts(file_path: str) -> List[List[str]]:
    temp_list = []
    str_count = 0
    words_count = []
    with open(file_path, 'r', encoding='UTF-8') as file:
        for line in file:
            temp_list.append(line.split())
            str_count += 1
    for el in temp_list:
        words_count.append(len(el))
    return str_count, words_count

# Print system messages with calculations result
str_count, words_count = get_counts(file_path)
print(f'The quantity of strings in file: {str_count}')
sys_message = []
while str_count:
    el = f'The quantity of words in {str_count} string: {words_count[str_count - 1]}'
    sys_message.append(el)
    str_count -= 1
sys_message.reverse()
for el in sys_message:
    print(el)

