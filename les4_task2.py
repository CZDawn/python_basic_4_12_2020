'''

2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

'''

default_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = []
for i in range(len(default_list)-1):
    if default_list[i] < default_list[i+1]:
        result_list.append(default_list[i+1])

print(result_list)

