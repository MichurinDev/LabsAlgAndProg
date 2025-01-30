from Lenght import lenght

# Задача 1
print("Задача 1")
sentence = input("Введите предложение: ")
output = ''

for i in range(lenght(sentence) - 1):
    s1 = sentence[i]
    s2 = sentence[i + 1]

    if s1 == s2 and not output:
        output = f"{i + 1} {i + 2}"

if not output:
    print("Предложение не содержит повторяющихся символов")


# Задача 2
print("\nЗадача 2")
sentence = input("Введите предложение: ")

output = ''
i = 0
comma_counter = 0

while (i < lenght(sentence)) and comma_counter != 2:
    if sentence[i + 1] == ',':
        comma_counter += 1

    if (comma_counter == 1) and (sentence[i + 1] != ','):
        output += sentence[i + 1]

    i += 1

print(output)

# Задача 3
print("\nЗадача 3")
sentence = input("Введите предложение: ").lower()
i = 0

while sentence[i] not in "ст":
    i += 1
else:
    print(sentence[i] + " встретилось раньше")
