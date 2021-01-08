'''

7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.

'''

class ComplexInteger:
    def __init__(self, integer: complex):
        self.__integer = integer

    def __add__(self, other: complex):
        return ComplexInteger(self.__integer + other.__integer)

    def __mul__(self, other: complex):
        return ComplexInteger(self.__integer * other.__integer)


complex_1 = (1+2j)
complex_2 = (-2+3j)

print(complex_1 + complex_2)
print(complex_1 * complex_2)
