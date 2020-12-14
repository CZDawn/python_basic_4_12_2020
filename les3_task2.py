'''

2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

'''

def info(**kwargs):
    result = name + ' ' + surname + ', ' + year_of_birth + ', ' + city_of_living + ', ' + email + ', ' + phone + '.'
    return result

name = input('What is your name?\n>>>')
surname = input('What is your surname?\n>>>')
year_of_birth = input('When you were born? (year)\n>>>')
city_of_living = input('Where you live?\n>>>')
email = input('Enter your e-mail.\n>>>')
phone = input('Enter your phone number.\n>>>')

user_data = info(arg_1=name, arg_2=surname, arg_3=year_of_birth, arg_4=city_of_living, arg_5=email, arg_6=phone)
print(user_data)
print(type(user_data))

