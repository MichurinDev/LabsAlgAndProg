# Написать функцию, печатающую все целые числа от a до b включительно
# (a ≤ b, не забудьте это проверить)

def f(a: int, b: int):
    if a <= b:
        for i in range(a, b+1):
            print(i)


def f_rec(a: int, b: int):
    if a <= b:
        print(a)
        f_rec(a+1, b)


f(1, 5)
print("---")
f_rec(1, 5)
