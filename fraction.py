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
        return delitel/value1

    def __add__(self, other) -> "Fraction":
        # nok = self.nok(self.denominator, other.denominator)
        del_number_self = self.nok(self.denominator, other.denominator) / self.denominator
        del_number_self = self.nok(self.denominator, other.denominator) / self.denominator
        del_number_other = self.nok(self.denominator, other.denominator) / other.denominator
        return Fraction((self.numerator * del_number_self) + (other.numerator * del_number_other),\
                        self.nok(self.denominator, other.denominator))

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

    # def __sub__(self, other) -> "Fraction":


frac1 = Fraction(1, 2)
frac2 = Fraction(1, 3)

result = frac1 + frac2
print(result)
