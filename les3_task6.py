'''

6. Реализовать функцию int_func(),
принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().

'''
def int_func(some_string: str):
    return some_string.title()

some_string = input('Enter string of word from little leter.\n>>>')
print(int_func(some_string))

'''

Alternative way:

def int_func(some_string: str):
    return ''.join((some_string[0].upper(), some_string[1:])) if some_string else some_string

def user_temp(some_string: str):
    return ' '.join(map(int_func, some_string.split(' ')))

'''


