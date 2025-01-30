a = int(input("Введите начало: "))
b = int(input("Введите конец: "))
counter = 0

for i in range(a, b + 1):
    flag = True
    for d in range(2, i):
        if i % d == 0:
            flag = False
    if flag:
        print(i)
        counter += 1

print(f"Количество простых чисел от {a} до {b}: {counter}")
