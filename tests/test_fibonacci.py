import my_lib
import pytest


# Тест функции, находящей простые числа, меньше заданного n
class TestFibonacci:

    # Тестируем программу на коррктных данных. Функция возвращает списко элементов.
    def test_on_correct_n(self):
        assert my_lib.fibonacci(6) == [0, 1, 1, 2, 3, 5]

    # Тестируем программу на некоррктных данных.
    def test_on_minus(self):
        assert my_lib.fibonacci(-1) == []

    # Тестируем программу на нуле.
    def test_on_zero(self):
        assert my_lib.fibonacci(0) == []

    def test_on_str(self):
        # Когда мы подаем на вход программе строку или букву - функция завершается с ошибкой.
        # Данная строчка показывает, что внутри блока кода под ней должно возникнуть заданное исключение
        # и это нормальное поведение.
        with pytest.raises(TypeError):
            my_lib.fibonacci("abc")