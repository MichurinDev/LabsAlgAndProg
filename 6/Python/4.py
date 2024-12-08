# Разработайте функцию, которая принимает список в качестве аргумента и 
# возвращает самое большое значение в списке. Используем операторы ветвления 
# для нахождения максимального значения.

def lenght(l: list) -> int:
    count = 0
    for _ in l: count += 1
    return count


def f(l: list) -> int:
    max_num = 0
    for n in l:
        if n > max_num:
            max = n
    return max


def f_rec(l: list) -> int:
    if lenght(l) == 1:
        return l[0]
    else:
        if l[0] > f_rec(l[1:]):
            return l[0]
        return f_rec(l[1:])


arr = [1, 2, 3, 7, 1, 6, 8]

print(f(arr))
print("---")
print(f_rec(arr))
