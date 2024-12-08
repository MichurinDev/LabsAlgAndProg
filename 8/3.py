# Реализуйте алгоритм, который находит минимальное значение в двумерном массиве 
# и его индексы (строку и столбец). Не используя встроенную функцию min(). 

import numpy as np

N = int(input("Кол-во строк: "))
M = int(input("Кол-во столбцов: "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = np.random.randint(a, b, size=(N, M))
print(f"Исходный массив: {arr}")

min_value = None
min_index = ()

for i in range(N):
    for j in range(M):
        if not min_value or arr[i][j] < min_value:
            min_value = arr[i][j]
            min_index = (i, j)

print(f"Минимальное значение: {min_value}")
print(f"Индексы минимального значения: {min_index}")
