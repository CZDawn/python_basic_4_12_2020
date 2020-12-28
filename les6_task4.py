'''

4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

'''

class Car:

    def __init__(self, color, name, is_police: bool = True):
        self.speed = 50
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return 'Car is start moving!'

    def stop(self):
        return 'Car stopped!'

    def turn(self, direction):
        self.dicertion = direction
        return f'Car turn {self.direction}'

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print('Speed over limit!')
        super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):

    def __init__(self, color, name):
        super().__init__(color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print('Speed over limit!')
        super().show_speed()

class PoliceCar(Car):
    pass

town_car = TownCar('green', 'Antony')
work_car = WorkCar('black', 'Jone')
town_car.show_speed()
work_car.show_speed()

