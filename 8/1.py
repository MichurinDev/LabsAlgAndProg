# Создайте вектор (одномерный массив) со значениями от 5 до 10 и разверните вектор
# (первый становится последним).

import numpy

vector = numpy.arange(5, 11)
print(vector)
print(vector[::-1])
