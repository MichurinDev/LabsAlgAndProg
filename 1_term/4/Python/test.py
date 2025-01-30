from Lenght import lenght


def count_by_symbol(s: str, symb: str) -> int:
    counter = 0
    for i in s:
        if i == symb:
            counter += 1
    return counter


s1 = input("Введите первую строку: ")
s2 = input("Введите вторую строку: ")
temp_str = ""
count = 0

if lenght(s1) == lenght(s2):
    for i in s1:
        if count_by_symbol(s1, i) == count_by_symbol(s2, i):
            if i not in temp_str:
                temp_str += i
            count += 1

if count == lenght(s1):
    print("Аннаграмма")
else:
    print("Не аннаграмма")
