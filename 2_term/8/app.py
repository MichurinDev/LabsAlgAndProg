# Хэш-таблица:
# 9. Сортировка по частоте: Напишите программу, которая принимает список чисел и 
# сортирует его по частоте появления элементов, используя хэш-таблицу.

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return

    def print_table(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

def sort_by_frequency(lst):
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_lst = sorted(lst, key=lambda x: (-freq_dict[x], x))
    return sorted_lst


print(sort_by_frequency([1, 2, 3, 2, 1, 3, 3, 4, 4, 4]))
