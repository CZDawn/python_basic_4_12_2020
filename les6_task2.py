'''

2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500т

'''

class Road:
    __asphalt_mass = 25

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_sum(self, thickness=5):
        return self._length * self._width * self.__asphalt_mass * thickness / 1000

length = input('Enter the length of road (in meters):\n>>>')
width = input('Enter the width of road (in meters):\n>>>')
asphalt_mass = Road(length, width)
print(f'The mass of asphalt for that length and width of road is: {asphalt_mass.asphalt_sum()} tons.')

