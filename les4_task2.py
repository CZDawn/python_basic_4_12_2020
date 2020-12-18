'''

2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.

'''

my_list = list(input('Enter some integers devided by spaces.\n>>>').split())
my_list = [int(el) for el in my_list if el.isdigit()]
new_list = [el + 10 for el in my_list]

print(f'Default list: {my_list}')
print(f'New list (aded 10 to elements): {new_list}')

