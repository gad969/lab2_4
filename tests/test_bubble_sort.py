import my_lib
import pytest

# Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
class TestIsBubbleOrdered:

    # Функция возвращает список чисел для сортировки
    @pytest.fixture
    def random_example(self):
        return [9, 2, 5, 3, -11]

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_random(self, random_example):
        assert my_lib.bubble_sort(random_example) == [-11, 2, 3, 5, 9]

    def test_on_str(self):
        # Когда мы подаем на вход программе список содержащий буквы и цифры - функция завершается с ошибкой.
        # Данная строчка показывает, что внутри блока кода под ней должно возникнуть заданное исключение
        # и это нормальное поведение.
        with pytest.raises(TypeError):
            my_lib.bubble_sort(['d', 1, 'f', 7, 'h'])