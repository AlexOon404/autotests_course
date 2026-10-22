# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

class TestTask4:

    def test_minus(self):
        assert all_division(-50, 10, -5) == 1

    def test_zero(self, time_work):
        time_work
        with pytest.raises(ZeroDivisionError):
            assert all_division(4, 1, 0, 2)

    def test_float(self):
        assert all_division(25.5, 2.5, 12) == 0.85

    def test_first_zero(self):
        assert all_division(0, 2, 10000, 2345) == 0

    def test_plus(self):
        assert all_division(300, 25, 6, 2) == 1

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
