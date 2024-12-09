# Создайте массив NxM (N и M вводятся с клавиатуры) и выберите координату-ячейку 
# (номер строки и столбца). Напишите функцию, выделяющую часть массива 
# фиксированного размера с центром в данной координате-ячейке.

import numpy as np

def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def minimum(*args):
    arr = list(args)
    return sort(arr)[0]


def maximum(*args):
    arr = list(args)
    return sort(arr)[-1]
    

def extract_subarray(array: np.ndarray, center_row: int, center_col: int, size):
    row_count, col_count = size

    if center_row == 0 or center_row == row_count - 1 or center_col == 0 or center_col == col_count - 1:
        return [[array[center_row, center_col]]]

    half_size = minimum(center_col + 1, center_row + 1, row_count - center_row, col_count - center_col) - 1

    start_row = maximum(center_row - half_size, 0)
    end_row = minimum(center_row + half_size + 1, array.shape[0])
    start_col = maximum(center_col - half_size, 0)
    end_col = minimum(center_col + half_size + 1, array.shape[1])

    subarray = array[start_row:end_row, start_col:end_col]
    
    return subarray


N = int(input("Кол-во строк: "))
M = int(input("Кол-во столбцов: "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = np.random.randint(a, b, size=(N, M))
print(f"Исходный массив: {arr}")

center_row = int(input("Введите индекс строки центра: "))
center_col = int(input("Введите индекс столбца центра: "))

subarray = extract_subarray(arr, center_row, center_col, (N, M))
print(f"Извлеченный подмассив:\n{subarray}")
