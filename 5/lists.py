import math
from Lenght import len

# СПИСКИ
arr1 = [2, 3, 8, 6, 1]
print(f'Исходный список: {arr1}')

# Задача 1
print("Задача 1")
print(arr1[0] - arr1[-1])

# Задача 2
print("\nЗадача 2")
print(arr1.index(arr1[0] + arr1[-1]))

# Задача 3
print("\nЗадача 3")
print(arr1[len(arr1) // 2] == arr1[0] * arr1[-1])

# Задача 4
print("\nЗадача 4")
mult = 1
for i in arr1:
    mult *= i

print(math.factorial(len(arr1)) == mult)

# Задача 5
print("\nЗадача 5")
print(all(len(str(i)) == 3 for i in arr1))

# Задача 6
print("\nЗадача 6")
print(all(i % 2 == 0 for i in arr1))

# Задача 7
print("\nЗадача 7")
arr2 = [1, 24, 6, 8, 7, 10, 4]
i = int(input("Введите индекс элемента: "))
print(arr1[i] in arr2)

# Задача 8
print("\nЗадача 8")
arrs = [[2, 5, 1, 86, 2], [2, 3, 0, 10, -9], [5, 30, 2], [1], [8, 5, 4]]
num = int(input("Введите число: "))
print([num in arr for arr in arrs].count(True))

# Задача 9
print("\nЗадача 9")
output = [arr1[-1]] + arr1[1:-1] + [arr1[0]]
print(output)

# Задача 10
print("\nЗадача 10")
i, j = int(input("Введите 1-й индекс: ")), int(input("Введите 2-й индекс: "))
output = arr1[:i] + [arr1[j]] + [arr1[i]] + arr1[j+1:]
print(output)

# Задача 11
print("\nЗадача 11")
output = [arr1[-2]] + arr1
print(output)

# Задача 12
print("\nЗадача 12")
output = []
if arr1[0] < arr1[1]:
    output = [arr1[0] * 2] + arr1[1:]
else:
    output = arr1

print(output)
