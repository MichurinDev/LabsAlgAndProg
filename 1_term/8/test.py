import numpy as np

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
matrix = np.random.randint(1, 100, size=(n, m))

print("Исходная матрица:")
print(matrix)

i = 1
j = 3

center_i, center_j = n // 2, m // 2

if i != center_i:
    matrix[[center_i, i]] = matrix[[i, center_i]]

if j != center_j:
    matrix[:, [center_j, j]] = matrix[:, [j, center_j]]

print("\nМатрица после перемещения элемента в центр:")
print(matrix)
