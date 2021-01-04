'''

3. Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
введя, например, команду “stop”. При этом скрипт завершается,
сформированный список выводится на экран.

Подсказка: для данного задания примем,
что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента
необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число.

Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

'''

class OwnException(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def my_method(element):
        try:
            element = int(element)
            return element
        except ValueError:
            print('You entered not an integer - it would not append at list!')
            return False

some_list = []
while True:
    element = input('Enter an integer or string. If you want stop - enter STOP:\n>>>')
    element = element.lower()
    if element == 'stop':
        break
    else:
        item = OwnException.my_method(element)
        if item != False:
            some_list.append(item)
            continue

print(some_list)

