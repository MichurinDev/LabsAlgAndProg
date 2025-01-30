# Задание 1
def f(x: float) -> float:
    if x < 5:
        return 16 * x ** 4 - 16
    elif 5 <= x <= 20:
        return 2 * x ** 7  + x ** 2 - 321
    else:
        return x / 19 - x ** 2 + 5

print(f(float(input("x = "))))

# Задание 2
a, b, c = float(input("a = ")), float(input("b = ")), float(input("c = "))
print(bool(a and b and c))
print(bool(a or b or c))
print(bool(a or b and c))
print(bool(a and b or c))

print(bool(not a and b and c))
print(bool(a and not b and c))
print(bool(a and b and not c))
print(bool(not a and not b and c))
print(bool(a and not b and not c))
print(bool(not a and b and not c))
print(bool(not a and not b and not c))

print(bool(not a or b or c))
print(bool(a or not b or c))
print(bool(a or b or not c))
print(bool(not a or not b or c))
print(bool(a or not b or not c))
print(bool(not a or b or not c))
print(bool(not a or not b or not c))

print(bool(not a or b and c))
print(bool(a or not b and c))
print(bool(a or b and not c))
print(bool(not a or not b and c))
print(bool(a or not b and not c))
print(bool(not a or b and not c))
print(bool(not a or not b and not c))

print(bool(not a and b or c))
print(bool(a and not b or c))
print(bool(a and b or not c))
print(bool(not a and not b or c))
print(bool(a and not b or not c))
print(bool(not a and b or not c))
print(bool(not a and not b or not c))
