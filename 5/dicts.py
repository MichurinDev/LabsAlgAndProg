# СЛОВАРИ
# Задача 1
print("Задача 1")
telephone_book = {
    "Иван": "33-89-01",
    "Петр": "63-52-00",
    "Аркадий": "33-85-95"
}

for name, number in telephone_book.items():
    if number[:2] == "33":
        print(name, number)

# Задача 2
print("\nЗадача 2")
normatives = {
    "run" : 10,
    "jump": 160
}

results = {
    "Иван": {
        "run" : 10,
        "jump" : 200
    },
    "Петр" : {
        "run" : 9,
        "jump" : 190
    },
    "Андрей" : {
        "run" : 20,
        "jump" : 100
    },
    "Мария" : {
        "run" : 12,
        "jump" : 165
    },
    "Екатерина" : {
        "run" : 8,
        "jump" : 200
    }
}

noncomplite_normatives_name = []
for name in results:
    if results[name]["run"] > normatives["run"] and results[name]["jump"] < normatives["jump"]:
        noncomplite_normatives_name.append(name)

complite_normatives_counter = len(results) - len(noncomplite_normatives_name)

best_runners = []
best_jumpers = []
scores = {name: 0 for name in results}

best_run_result = sorted([(name, results[name]["run"]) for name in results if name not in noncomplite_normatives_name], key=lambda x: x[1])[:3]
for name, _ in best_run_result:
    scores[name] += 1

best_jump_result = sorted([(name, results[name]["jump"]) for name in results if name not in noncomplite_normatives_name], key=lambda x: x[1], reverse=True)[:3]
for name, _ in best_run_result:
    scores[name] += 1

best_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:3]

print(f"Не выполнили нормативы: {', '.join(noncomplite_normatives_name)}")
print(f"Норамативы выполнили (человек): {complite_normatives_counter}")
print(f"Лучшие результаты у следующих участников:\nI - {best_results[0][0]},\nII - {best_results[1][0]},\nIII - {best_results[2][0]}")

# Задача 3
print("\nЗадача 3")

items = {
    "Картофель": (10, 12),
    "Морковь": (15, 12),
    "Свекла": (15, 40)
}

print("Ожидавется повышение цены на следующие позиции:")
for name, (old_price, new_price) in items.items():
    if old_price < new_price:
        print(f"{name}: {old_price}₽ -> {new_price}₽ (на {round((new_price - old_price) / old_price * 100, 1)}%)")


# Задача 4
print("\nЗадача 4")

synonims = {
    "атака": "наступление",
    "красивый": "прекрасный",
    "спешить": "торопиться",
    "земля": "почва",
    "кругом": "вокруг"
}

print(list(synonims.values())[-1])

# Задача 5
print("\nЗадача 5")

countries_and_cities = {
    "Россия": ["Москва", "Санкт-Петербург", "Новосибирск", "Екатеринбург"],
    "Украина": ["Киев", "Львов", "Одесса", "Харьков"],
    "Беларусь": ["Минск", "Гомель", "Витебск", "Могилев"],
    "Казахстан": ["Алматы", "Шымкент", "Усть-Каменогорск", "Атырау"]
}

for country, cities in countries_and_cities.items():
    for city in cities:
        print(f"{city} - {country}")
    print()

# Задача 6
print("\nЗадача 6")
birthdays = {
    "Мичурин А. К.": "20.05.2006",
    "Якупов О. Л.": "20.05.2007",
    "Елизарова А. К.": "19.04.2007",
    "Петраев С. С.": "01.01.2006",
    "Метов К. О.": "31.12.2005",
    "Горшков П. П.": "30.11.2006"
}

sum_days = 0
sum_mothes = 0
sum_years = 0

for name, birthday in birthdays.items():
    birthday_list = birthday.split(".")
    sum_days += int(birthday_list[0])
    sum_mothes += int(birthday_list[1])
    sum_years += int(birthday_list[2])

print(f"День рождения класса: {round(sum_days / len(birthdays))}.{round(sum_mothes / len(birthdays))}.{round(sum_years / len(birthdays))}")

# Задача 7
print("\nЗадача 7")
ankets = {
    "Мичурин": 18,
    "Якупов": 17,
    "Елизарова": 17,
    "Петраев": 18,
    "Метов": 19,
    "Горшков": 18
}

age_layers = {

}

for name, age in ankets.items():
    if age in age_layers:
        age_layers[age].append(name)
    else:
        age_layers[age] = [name]

for age, names in sorted(age_layers.items(), key=lambda x: x[0]):
    print(f"{age} лет: {', '.join(names)}")

# Задача 8
print("\nЗадача 8")
ankets = {
    "Мичурин": [5, 4, 4, 3, 2, 5, 4, 4, 2],
    "Якупов": [3, 3, 5, 3, 4, 3, 2, 4, 5],
    "Елизарова": [5, 5, 5, 4, 4, 5, 4, 3, 5],
    "Петраев": [2, 2, 2, 3, 4, 3, 5, 4, 4],
    "Метов": [4, 2, 3, 4, 3, 2, 5, 4, 2],
    "Горшков": [3, 5, 5, 5, 4, 3, 5, 4]
}

academic_achievement_percentage = 0
percentage_of_quality = 0

fives_counts = 0
fours_counts = 0
threes_counts = 0
grades_counter = 0

for _, grades in ankets.items():
    fives_counts += grades.count(5)
    fours_counts += grades.count(4)
    threes_counts += grades.count(3)
    grades_counter += len(grades)

academic_achievement_percentage = round((fives_counts + fours_counts + threes_counts) / grades_counter * 100, 2)
percentage_of_quality = round((fives_counts + fours_counts) / grades_counter * 100, 2)

print(f"Процент успеваемости (абсолютная успеваемость): {academic_achievement_percentage}%")
print(f"Процент качества знаний (качественная успеваемость): {percentage_of_quality}%")
