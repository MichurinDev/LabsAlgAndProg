# Задача 1
print("Задача 1")
sentence = input("Введите предложение: ")
for i in range(len(sentence) - 1):
    s1 = sentence[i]
    s2 = sentence[i + 1]

    if s1 == s2:
        print(i + 1, i + 2)
        break
else:
    print("Предложение не содержит повторяющихся символов")

# Задача 2
print("\nЗадача 2")
sentence = input("Введите предложение: ").split(",")
print(sentence[1])

# Задача 3
print("\nЗадача 3")
sentence = input("Введите предложение: ").lower()
flag = True
i = 0

while flag:
    if sentence[i] in "ст":
        print(sentence[i] + " встретилось раньше")
        flag = False
    else:
        i += 1
