from Lenght import len

# Задача 1
print("Задача 1")
print(f"Столица государства {input('Введите страну: ')} — город {input('Введите город: ')}")

# Задача 2
print("\nЗадача 2")
surname1 = input("Введите фамилию: ")
surname2 = input("Введите фамилию: ")

if len(surname1) > len(surname2):
    print(f"{surname1} длинее")
else:
    print(f"{surname2} длинее")

# Задача 3
print("\nЗадача 3")
city1 = input("Введите город: ")
city2 = input("Введите город: ")
city3 = input("Введите город: ")

if len(city1) > len(city2):
    if len(city1) > len(city3):
        print(f"Самое длинное {city1}")
    else:
        print(f"Самое длинное {city3}")
else:
    if len(city2) > len(city3):
        print(f"Самое длинное {city2}")
    else:
        print(f"Самое длинное {city3}")

if len(city1) < len(city2):
    if len(city1) < len(city3):
        print(f"Самое короткое {city1}")
    else:
        print(f"Самое короткое {city3}")
else:
    if len(city2) < len(city3):
        print(f"Самое короткое {city2}")
    else:
        print(f"Самое короткое {city3}")

# Задача 4
print("\nЗадача 4")
s1 = input("Введите первую страну: ")
s2 = input("Введите вторую страну: ")

s1, s2 = s2, s1
print(f"{s1} и {s2} поменялись местами")
