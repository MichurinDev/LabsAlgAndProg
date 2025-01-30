from utils import *


def sort_tuples(tuples, n):
    data = list(tuples)
    n -= 1

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][n] > data[j][n]:
                data[i], data[j] = data[j], data[i]

    return tuple(data)

    
# КОРТЕЖИ
# Задача 1
symbs = (s for s in input("Введите строку: "))
for s in symbs:
    print(s)

# Задача 2
nums = tuple(float(s) for s in input("Введите числа через пробел: ").split())
max_num, min_num = None, None

for num in nums:
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num

print(min_num, max_num, min_num + max_num)

# Задача 3
data = (
    ('красный', 33, 55),
    ('зеленый', 17, 44),
    ('синий', 12, 3),
    ('черный', 2, 5)
)
print(sort_tuples(data, 3))

# Задача 4
line = (input("Введите символы через пробел: ").split())
print(count(line, line[0]) == lenght(line))
