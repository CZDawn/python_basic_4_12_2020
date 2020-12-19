'''

2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

'''

my_list = list(input('Enter some integers devided by spaces.\n>>>').split())
my_list = [int(el) for el in my_list if el.isdigit()]

new_list = []
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        new_list.append(my_list[i+1])

print(f'Default list: {my_list}')
print(f'New list: {new_list}')

