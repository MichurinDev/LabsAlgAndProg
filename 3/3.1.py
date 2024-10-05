import math

def f(x: float) -> float:
    return (math.sin(x) / (math.log(x) ** 2)) + (math.cos(x) / (math.log(abs(x))))


print(f"x\t|y")
print("+-----------------------------+")

# Способ 1
for i in range(2, 3):
    for j in range(10):
        num = round((i * 10 + j) / 10, 1)
        print(f"{num}\t|{f(num)}")

num += 0.1
print(f"{num}\t|{f(num)}")

print("+-----------------------------+")

# Способ 2
i = 2
while i < 3.1:
    num = round(i, 1)
    print(f"{num}\t|{f(num)}")
    i += 0.1
