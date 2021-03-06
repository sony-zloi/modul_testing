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
#  - Дробь может быть неупрощенной (12/3 -> 4/1)
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

    def __init__(self, num: int, den: int):
        self.num = num
        if den:
            self.den = den
        else:
            raise ZeroDivisionError

    @staticmethod
    def getNok(value1: int, value2: int) -> int:
        """Получение наименьшего общего кратного"""
        if value1 > value2:
            delitel = value1
        else:
            delitel = value2

        while True:
            if delitel % value1 == 0 and delitel % value2 == 0:
                break
            delitel += 1
        return delitel

    def __add__(self, other) -> "Fraction":
        # nok = self.nok(self.den, other.den)
        # del_number_self = self.nok(self.den, other.den) / self.den
        del_number_self = self.getNok(self.den, other.den) / self.den
        del_number_other = self.getNok(self.den, other.den) / other.den
        return Fraction(int((self.num * del_number_self) + (other.num * del_number_other)),\
                        self.getNok(self.den, other.den))

    def __repr__(self):
        return f"{self.num}/{self.den}"

    def __sub__(self, other) -> "Fraction":
        del_number_self = self.getNok(self.den, other.den) / self.den
        del_number_other = self.getNok(self.den, other.den) / other.den
        return Fraction(int((self.num * del_number_self) - (other.num * del_number_other)),\
                        self.getNok(self.den, other.den))

    def __mul__(self, other) -> "Fraction":
        return Fraction((self.num * other.num), (self.den * other.den))

    def __truediv__(self, other) -> "Fraction":
        return Fraction((self.num * other.den), (self.den * other.num))

    def __pow__(self, power, modulo=None):
        return Fraction((self.num ** power), (self.den ** power))

frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)

result = frac1 / frac2
print(result)
pow1 = frac2 ** 2
print(pow1)
