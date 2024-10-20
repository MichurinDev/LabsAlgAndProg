# МНОЖЕСТВА
# Задача 1
print("Задача 1")
word = input("Введите слово: ")
output = set()
for i in word:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        output.add(i.lower())
print(len(output))

# Задача 2
print("\nЗадача 2")
symbs = ['а', 'е', 'о', 'у', 'ы', 'э', 'ю', 'я', 'и', 'ё']
text = input("Введите текст: ")
output = set()

for s in text:
    if s.lower() in symbs:
        output.add(s.lower())
print(sorted(output))

# Задача 3
print("\nЗадача 3")
text = input("Введите текст: ")

word_grabber_a = set()
output_b = set()
output_c = set()

print("а)")
for word in text.split():
    for s in word:
        if s.lower() not in word_grabber_a:
            word_grabber_a.add(s.lower())
            print(f"{s.lower()}: {word}")

for s in text:
    if text.count(s) >= 2:
        output_b.add(s)

for s in text:
    if text.count(s) == 1:
        output_c.add(s)

print(f"б) {output_b}")
print(f"в) {output_c}")

# Задача 4
print("\nЗадача 4")
symbs = set(input("Введите строку: "))
uniq_symbs = 0
for s in symbs:
    if s in "0123456789+-*":
        uniq_symbs += 1
print(uniq_symbs)

# Задача 5
print("\nЗадача 5")
M = set(i for i in range(100))
A = (1, -9, 962, 1, 456262, -196)
uniq_symbs = 0

for i in A:
    if i in M:
        uniq_symbs += 1

print(uniq_symbs)

# Задача 6
print("\nЗадача 6")
nums = set(input("Введите число: "))
uniq_symbs = 0
for i in nums:
    if i != "0":
        uniq_symbs += 1

print(uniq_symbs)

# Задача 7
print("\nЗадача 7")
vowels_counter = 0
consonants_counter = 0
text = input("Введите текст: ")

for s in text:
    if s in ['a', 'e', 'i', 'o', 'u']:
        vowels_counter += 1
    elif s in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']:
        consonants_counter += 1

if vowels_counter > consonants_counter:
    print("Гласных больше")
elif vowels_counter < consonants_counter:
    print("Согласных больше")
else:
    print("Одинаковое количество гласных и согласных")

# Задача 8
print("\nЗадача 8")
line = set(input("Введите строку: ").lower())
uniq_symbs = set()

for s in line:
    if s.isdigit() or s.isalpha():
        uniq_symbs.add(s)

print(len(uniq_symbs), uniq_symbs)
