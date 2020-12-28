'''

3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).

'''

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_position(self):
        return f'{self.position}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']

name = input('Enter your name:\n>>>')
surname = input('Enter your surname:\n>>>')
position = input('Enter your position:\n>>>')
wage = input('Enter your wage in rubles:\n>>>')
bonus = input('Enter your bonus un rubles:\n>>>')

if wage.isdigit() and bonus.isdigit():
    wage = int(wage)
    bonus = int(bonus)
else:
    print('You should enter an integer in wage and bonus categoty!')

result = Position(name, surname, position, wage, bonus)
print(result.get_full_name())
print(result.get_position())
print(result.get_total_income())

