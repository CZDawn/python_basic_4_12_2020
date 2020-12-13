'''

5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

'''

my_list = [8, 7, 6, 5, 4, 3, 2, 1]
while True:
    agreement = input('Do you want to enter a digit? enter Y or N.\n>>>')
    agreement = agreement.lower()
    if agreement == 'y':
        some_number = input('Enter some number.\n>>>')
        if some_number.isdigit():
            some_number = int(some_number)
            my_list.append(some_number)
            my_list.sort(reverse=True)
        else:
            print('You have entered not a digit! Try again!')
    elif agreement == 'n':
        break
    else:
        print('You have to make a choise!')

print(my_list)

