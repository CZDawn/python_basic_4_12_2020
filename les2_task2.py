'''

2. Для списка реализовать обмен значений соседних элементов,
т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

'''

some_list = []

while True:
    agreement = input('Do you want to add some element to list? - enter Y or N\n>>>')
    agreement = agreement.lower()
    if agreement == 'y':
        some_el = input('Enter some element to add in list.\n>>>')
        some_list.append(some_el)
    elif agreement == 'n':
        print(f'Great job! Let see the created list: {some_list}')
        break
    else:
        print('You shoud make a choise: Y or N!')

i = 0
if len(some_list) % 2 == 0:
    while i < len(some_list):
        some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
        i += 2
else:
    while i < (len(some_list) - 1):
        some_list[i], some_list[i+1] = some_list[i+1], some_list[i]
        i += 2
print(f'Changed list is: {some_list}.')

