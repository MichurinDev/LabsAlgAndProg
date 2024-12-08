# Создайте массив NxM (N и M вводятся с клавиатуры) и выберите координату-ячейку 
# (номер строки и столбца). Напишите функцию, выделяющую часть массива 
# фиксированного размера с центром в данной координате-ячейке.

import numpy as np

def extract_subarray(array, center_row, center_col, size):
    half_size = size // 2

    start_row = max(center_row - half_size, 0)
    end_row = min(center_row + half_size + 1, array.shape[0])
    start_col = max(center_col - half_size, 0)
    end_col = min(center_col + half_size + 1, array.shape[1])

    subarray = array[start_row:end_row, start_col:end_col]
    
    return subarray


N = int(input("Кол-во строк: "))
M = int(input("Кол-во столбцов: "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = np.random.randint(a, b, size=(N, M))
print(f"Исходный массив: {arr}")

center_row = int(input("Введите номер строки центра: "))
center_col = int(input("Введите номер столбца центра: "))

size = int(input("Введите размер подмассива (нечетное число): "))

if size % 2 == 0:
    print("Размер подмассива должен быть нечетным. Программа завершена.")
else:
    subarray = extract_subarray(arr, center_row, center_col, size)
    print("Извлеченный подмассив:")
    print(subarray)
