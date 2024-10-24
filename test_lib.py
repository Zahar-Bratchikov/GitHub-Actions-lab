import pytest
from lib import fibonacci, bubble_sort, calculator


# Тест для функции calculator
def test_calculator():
    assert calculator(3, 2, '+') == 5
    assert calculator(3, 2, '-') == 1
    assert calculator(3, 2, '*') == 6
    assert calculator(6, 2, '/') == 3

    with pytest.raises(ValueError):
        calculator(3, 0, '/')  # Должно выбросить исключение деления на ноль

    with pytest.raises(ValueError):
        calculator(3, 2, 'i')  # Должно выбросить исключение неверной операции


# Тест для функции fibonacci
def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

    with pytest.raises(ValueError):
        fibonacci(0)  # Должно выбросить исключение для неверного ввода


# Тест для функции bubble_sort
def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([3]) == [3]
