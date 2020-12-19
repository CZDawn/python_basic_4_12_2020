'''

4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.

'''

some_string = input('Enter some words divided by spaces.\n>>>')
some_list = some_string.split()
for ind, el in enumerate(some_list, 1):
    print(ind, el[:10])

