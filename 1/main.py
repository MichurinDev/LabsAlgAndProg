import math as m

def f(x: float, a: float, b: float) -> float:
    return (b + m.sin(a*x) ** 2) / (m.e ** (-x / 2))

x = float(input("x = "))
a = float(input("a = "))
b = float(input("b = "))

y = f(x, a, b)
print(f'y = {y}')
