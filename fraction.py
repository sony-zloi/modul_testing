# Реализовать класс обыкновенной дроби (https://ru.wikipedia.org/wiki/%D0%94%D1%80%D0%BE%D0%B1%D1%8C_(%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B0))
# Добавить операции
# - сложения
# - вычитания
# - умножения
# - деления
# - возведения в степень
# Обратить внимание на следующие моменты
#  - Объект дроби иммутабельный (неизменяемый), при результатом матиематических операций/преобразований является новый объект
#  - Дробь может иметь целую часть (3/2 -> 1 1/2)
#  - Дробь может быть неупрощенной (12/3 -> 3)
#     * - релизовать метод упрощения, который вернет упрощеную дробь
#  - Дроби можно сравнивать, неупрощенные дроби должны быть равны упрощенной (12/3 = 4/1)
#  - Дробь можно преобразовать в число с плавающей точкой (передать в конструтор float) или получить целую часть от дроби
#    *для этого нужно реализовать соотвествующие методы __float__ и __int__
#  - Все математические операции должны работать и с обычными числами

# Все методы класса Fraction нужно протестировать
# Тесты писать в tests/test_fraction.py

from typing import *


class Fraction:
    """Здесь реализовать поля и методы"""

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    @staticmethod
    def nok(value1, value2) -> int:
        delitel = value1
        while True:
            if delitel % value1 == 0 and delitel % value2 == 0:
                break
            delitel += 1
        return delitel

    def __add__(self, other) -> "Fraction":
        nok = self.nok(self.denominator, other.denominator)
        del_number = nok/self.denominator
        return ((self.numerator * del_number) + (other.numerator * del_number)), nok


frac1 = Fraction(7, 5)
frac2 = Fraction(6, 7)

print(frac1 + frac2)
