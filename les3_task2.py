'''

2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

'''

def user_info(**kwargs):
    ''' Return string with user data

    named arguments (**kwargs):
    name -- user name (default - string)
    surname -- user surname (default - string)
    year -- user year of birth (default - string)
    city -- user city of living (default - string)
    email -- user email (default - string)
    phone -- user phone number (defaultt - string)

    >>> user_info(name='Ivan', surname='Ivanov', year_of_birth='2000', city='Moskow', email='info@gmail.com', phone='+7900000000')
    Ivan Ivanov, 2000, Moskow, info@gmail.com, +79000000000
    '''

    result = name + ' ' + surname + ', ' + year + ', ' + city + ', ' + email + ', ' + phone + '.'
    return result


name = input('What is your name?\n>>>')
surname = input('What is your surname?\n>>>')
year = input('When you were born? (year)\n>>>')
city = input('Where you live?\n>>>')
email = input('Enter your e-mail.\n>>>')
phone = input('Enter your phone number.\n>>>')


user_data = user_info(arg_1=name, arg_2=surname, arg_3=year, arg_4=city, arg_5=email, arg_6=phone)
print(user_data)

