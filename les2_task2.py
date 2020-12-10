'''

2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

'''
import ast
some_list = []

while True:
    agreement = input('Do you want to add some element to list? - enter Y or N')
    agreement = agreement.lower()
    if agreement == 'y':
        some_el = input('Enter some element to add in list')
        some_list.append(ast.literal_eval(some_el))
    elif agreement == 'n':
        print(f'Great job! Let see the created list: {some_list}')
        break
    else:
        print('You shoud make a choise: Y or N!')

