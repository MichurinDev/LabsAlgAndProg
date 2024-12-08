# Проверка симметрии. Напишите функцию, которая проверяет, является ли заданная 
# квадратная матрица симметричной относительно главной диагонали. Количество 
# строк и столбцов вводится с клавиатуры.

import numpy as np

N = int(input("Введите N (матрица N x N): "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = np.random.randint(a, b, size=(N, N))
print(f"Исходная матрица: {arr}")

is_symmetric = True
for i in range(N):
    for j in range(N):
        if arr[i][j] != arr[j][i]:
            is_symmetric = False

if is_symmetric:
    print("Матрица является симметричной")
else:
    print("Матрица не является симметричной")
