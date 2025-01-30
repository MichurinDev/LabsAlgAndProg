# Массив NxM, заполнить значениями 1-5
import numpy as np

n = int(input("Кол-во строк: "))
m = int(input("Кол-во столбцов: "))

arr = np.random.randint(1, 6, size=(n, m))
print(arr)
cols = arr[:, ::2]
print(cols)

max_sum = 0

for i in range(m // 2):
    col_sum = 0
    for j in range(n):
        col_sum += cols[j][i]

    if col_sum > max_sum:
        max_sum = col_sum

print(max_sum)
