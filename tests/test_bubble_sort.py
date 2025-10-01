import my_lib
import pytest

# Тест функции, которая проверяет, что значения во входном списке упорядочены от мин к макс
class TestIsBubbleOrdered:

    # Функция возвращает список чисел для сортировки
    @pytest.fixture
    def random_example(self):
        return [9, 2, 5, 3, 1]

    # Тест функции на упорядоченных от мин к макс значениях
    def test_on_random(self, random_example):
        assert my_lib.bubble_sort(random_example) == [1, 2, 3, 5, 9]