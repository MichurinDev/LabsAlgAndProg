# Задача 1
print("Задача 1")
word = input("Введите слово: ")
print(word[2])

# Задача 2
print("Задача 2")
word = input("Введите слово: ")
print(word[int(input("Введите номер символа: ")) - 1])

# Задача 3
print("Задача 3")
word = input("Введите слово: ").lower()
print(word[0] == word[-1])

# Задача 4
print("Задача 4")
word = input("Введите слово: ")
print(word[1] + word[3])

# Задача 5
print("Задача 5")
word = input("Введите слово: ")
print(word[1:4])

# Задача 6
print("Задача 6")
word = input("Введите слово: ")
print(word[:len(word) // 2])

# Задача 7
print("Задача 7")
word = input("Введите слово: ")
m = int(input("Начало: "))
n = int(input("Конец: "))
print(word[m-1:n+1])
