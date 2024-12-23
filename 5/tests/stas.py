dict_school_class = {
    "Самойлов": 13,
    "Ульянов": 14,
    "Кузнецова": 15,
    "Фомин": 16,
    "Басов": 17,
    "Моисеева": 14,
    "Зайцев": 13
}

groups = dict()

print("Список учеников и возраст")
for family, age in dict_school_class.items():
    print(f"Фамилия: {family}, возраст: {age}")
    if age not in groups:
        groups[age] = []
    groups[age].append(family)

for group, members in groups.items():
    print(f"Группа {group} лет: {', '.join(members)}")
