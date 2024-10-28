from Lenght import len

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
sentence = input("Введите предложение: ")

output = ''
i = 0
flag = True
comma_counter = 0

while (i < len(sentence)) and flag:
    if sentence[i + 1] == ',':
        comma_counter += 1

    if (comma_counter == 1) and (sentence[i + 1] != ','):
        output += sentence[i + 1]
    elif comma_counter == 2:
        flag = False

    i += 1

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
