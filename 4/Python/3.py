from Lenght import len

# Задача 1
print("Задача 1")
s = input("Введите слово: ")
new_s = ""

for i in s:
    new_s = i + new_s

print(new_s)

# Задача 2
print("Задача 2")
word = input("Введите слово: ")
print("*" * len(word) + word + "*" * len(word))

# Задача 3
print("\nЗадача 3")
word = input("Введите слово: ")

for i in range(2, len(word), 3):
    print(word[i])

# Задача 4
print("\nЗадача 4")
sentence = input("Введите предложение: ")
s1 = input("Введите первый символ: ")
s2 = input("Введите второй символ: ")
temp_str = ""

print(f"Вхождения символа {s1}")
for s in sentence:
    if s == " ":
        if s1 in temp_str:
            print(temp_str)
        temp_str = ""
    else:
        temp_str += s

print(f"\nВхождения символа {s2}")
for s in sentence:
    if s == " ":
        if s2 in temp_str:
            print(temp_str)
        temp_str = ""
    else:
        temp_str += s

# Задача 5
print("\nЗадача 5")
sentence = input("Введите предложение: ")
counter = 0
for s in sentence:
    if s == " ":
        counter += 1
print(counter)

# Задача 6
print("\nЗадача 6")
sentence = input("Введите предложение: ")
counter = 0

for i in range(len(sentence) - 1):
    s1 = sentence[i]
    s2 = sentence[i + 1]

    if s1 == s2:
        counter += 1

print(counter)
