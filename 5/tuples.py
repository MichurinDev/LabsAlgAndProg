from Lenght import len

# КОРТЕЖИ
# Задача 1
symbs = (s for s in input("Введите строку: "))
for s in symbs:
    print(s)

# Задача 2
nums = sorted((float(s) for s in input("Введите числа через пробел: ").split()))
print(nums[0], nums[-1], nums[0] + nums[-1])

# Задача 3
data = (('красный', 33, 55), ('зеленый', 17, 44), ('синий', 12, 3), ('черный', 2, 5))
print(sorted(data, key=lambda x: x[2]))

# Задача 4
line = (input().split())
print(line.count(line[0]) == len(line))
