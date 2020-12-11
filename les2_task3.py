'''

3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.

'''

# Solve task with dictionary
some_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
while  True:
    month_number = input('Enter the number of month.\n>>>')
    if month_number.isdigit():
        month_number = int(month_number)
        print(f'The {month_number} month is {some_dict.get(month_number)} month.')
        break
    else:
        print('Be careful, enter an integer!')

# Solve task with list
some_list = ['winter', 'spring', 'summer', 'autumn']
while True:
    month_number = input('Enter the number of month.\n>>>')
    if month_number.isdigit():
        month_number = int(month_number)
        if month_number < 3 or month_number == 12:
            print(f'The {month_number} month is {some_list[0]}.')
        elif month_number >= 3 and month_number < 6:
            print(f'The {month_number} month is {some_list[1]}.')
        elif month_number >= 6 and month_number < 9:
            print(f'The {month_number} month is {some_list[2]}.')
        elif month_number >= 9 and month_number < 12:
            print(f'The {month_number} month is {some_list[3]}.')
        else:
            print('There is no month with entered number!')
        break
    else:
        print('Be careful, enter an integer!')
