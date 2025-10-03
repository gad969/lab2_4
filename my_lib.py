import numpy as np

# Функция вывода списка значений чисел Фибоначи
# Принимает n, выводит список из n значений
def fibonacci(n):
    fib_sequence = []  # Создаем устой список
    a, b = 0, 1
    for i in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

#n - количество чисел Фибоначчи которые нужно вычислить
#n = 7
#print(fibonacci(n))


# Сортировка списка чисел пузьрьком
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1): # В цикле проходим список и сравниваем значения соседних элементов
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # если значение элемента больше чем значение следующего, меняим их местами

    return arr


#numbers = [2, 4, 9, 32, 1, 9]
#sorted_numbers = bubble_sort(numbers)
#print("Отсортированный список:", sorted_numbers)

# Функция поиска простых чисел методом Решето Эратосфена
# Принимает n возвращает список простых чисел < n
def find_primes(n):
    pre_primes = [] # Создаем пустой список
    for i in range(n): # Заполняем список числами по порядку
        pre_primes.append(i)
    pre_primes[1] = 0 # Заменяем второй элемент списока нулем (1 не явщяется простым числом)
    for i in range(2, n):
        if pre_primes[i]:
            for j in range(2*i, n, i): # Заменяем все не простые числа на ноль
                pre_primes[j] = 0
    primes = []
    for number in pre_primes: # В новый список вносим значения из списка pre_primes которые не равны нулю 
        if number:
            primes.append(number)
    return primes

#find_primes(-4)