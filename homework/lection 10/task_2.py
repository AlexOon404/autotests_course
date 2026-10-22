# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

@pytest.mark.acceptance
def test_minus():
    assert all_division(-50, 10, -5) == 1


@pytest.mark.smoke
def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert all_division(4, 1, 0, 2)


@pytest.mark.acceptance
def test_float():
    assert all_division(25.5, 2.5, 12) == 0.85

@pytest.mark.acceptance
def test_first_zero():
    assert all_division(0, 2, 10000, 2345) == 0

@pytest.mark.smoke
def test_plus():
    assert all_division(300, 25, 6, 2) == 1


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division




