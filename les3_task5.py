'''

5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

'''

def subtotal(*args):
    result = 0
    exit_flag = False
    for item in args:
        try:
            result += float(item) if item else 0
        except ValueError as e:
            if item == 'q':
                exit_flag = not exit_flag
                break
    return result, exit_flag

result_sum = 0

while True:
    some_string = input('Enter integers devided by spaces:\n>>>')
    result_subtotal, exit = subtotal(*some_string)
    result_sum += result_subtotal
    print(f'The sum of all integers that you have entered is - {result_sum}.')

    if exit:
        print('The end of program.')
        break

