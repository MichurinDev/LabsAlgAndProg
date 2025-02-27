import math


def f(x: float) -> float:
    return math.log(1.2 * x + 2.3) + ((math.e ** (3 * x)) * math.sinh(x))


def g(x: float) -> float:
    return 5 ** (x ** 2 + 1) * (x ** 3.3 + (abs(1 - x)) ** 0.5) ** 0.5


def h(x: float) -> float:
    return (1 + math.tan(x) ** 2) ** (math.atan(x) + math.log10(x) + 1)


a = float(input("a = "))
b = float(input("b = "))
x_start = float(input("начало = "))
x_end = float(input("конец = "))
x_delta = float(input("интервал = "))


print(f"x\t|y")
print("+-----------------------------+")

# Способ 1
for x in range(int(x_start), int(x_end) + 1, int(x_delta)):
    if x <= a:
        print(f"{x}\t|{f(x)}")
    elif a < x < b:
        print(f"{x}\t|{g(x)}")
    elif x >= b:
        print(f"{x}\t|{h(x)}")

print("+-----------------------------+")

# Способ 2
while x_start <= x_end:
    if x_start <= a:
        print(f"{int(x_start)}\t|{f(x_start)}")
    elif a < x_start < b:
        print(f"{int(x_start)}\t|{g(x_start)}")
    elif x_start >= b:
        print(f"{int(x_start)}\t|{h(x_start)}")
    x_start += x_delta
