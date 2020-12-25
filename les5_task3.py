'''

3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

'''
import os

file_path = os.path.join(os.path.dirname(__file__), 'task_3.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    my_dict = dict([line.split() for line in file])
    sys_messages = []
    sallary_less = []
    total_sallary = 0
    middle_sallary = 20000
    for i in my_dict:
        if my_dict[i].isdigit():
            my_dict[i] = int(my_dict[i])
        else:
            sys_messages.append(f'{i} sallary value is not an integer!')
        if my_dict[i] < middle_sallary:
            sallary_less.append(i)
        total_sallary += my_dict[i]
    for el in sys_messages:
        print(el)
    print('The values of sallary less 20000 rubles have:')
    for el in sallary_less:
        print(f'{sallary_less.index(el)+1} {el}')
    medium_sallary = total_sallary / len(my_dict)
    print(f'The medium sallary of workers is: {medium_sallary} rubles')

