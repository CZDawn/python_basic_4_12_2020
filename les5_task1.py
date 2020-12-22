'''

1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

'''

text = []
while True:
    some_text = input('Enter some text. If you want to fifnish just press enter.\n>>>')
    if some_text:
        text.append(some_text)
    elif not some_text:
        break

with  open('task_1.txt', 'w', encoding='UTF-8') as file:
    for item in text:
        file.write(item + '\n')

