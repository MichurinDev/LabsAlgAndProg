# Разработайте функцию, которая принимает целочисленный аргумент n и выводит 
# числа от 1 до n.

def f(n: int):
    for i in range(1, n+1):
        print(i)


def f_rec(n: int):
    if n > 0:
        f_rec(n-1)
        print(n)


f(5)
print("---")
f_rec(5)
