'''

1. Реализовать класс «Дата»,
функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.

'''

class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def convert_to_number(cls, date: str):
        day = int(date.split('-')[0])
        month = int(date.split('-')[1])
        year = int(date.split('-')[2])
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31 and 1 <= month <=12 and year > 0:
            print('Date is valid!')
        else:
            print('Date is invalid!!!')

if __name__ == '__main__':
    day, month, year = Date.convert_to_number('31-12-2020')
    Date.validation(day, month, year)
