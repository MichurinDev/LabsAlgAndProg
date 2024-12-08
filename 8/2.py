# Создайте массив NxM (N и M вводятся с клавиатуры). Напишите программу, которая 
# вычисляет сумму всех элементов двумерного массива целых чисел.  Не используя 
# встроенную функцию sum(). 

import numpy

N = int(input("Кол-во строк: "))
M = int(input("Кол-во столбцов: "))
a = int(input("Минимально значение генерируемого числа: "))
b = int(input("Максимальное значение генерируемого числа (не учитывается): "))

arr = numpy.random.randint(a, b, size=(N, M))
print(f"Исходный массив: {arr}")

total_sum = 0
for row in arr:
    for element in row:
        total_sum += element

print(f"Сумма: {total_sum}")
