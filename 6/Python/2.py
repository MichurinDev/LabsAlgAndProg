# Даны два целых числа a и b. Написать функцию, которая выводит все числа от a 
# до b включительно, в порядке возрастания, если a<b, или в порядке убывания в 
# противном случае.

def f(a: int, b: int):
    if a < b:
        for i in range(a, b+1):
            print(i)
    else:
        for i in range(a, b-1, -1):
            print(i)


def f_rec(a: int, b: int):
    if a <= b:
        if a == b:
            print(a)
        else:
            print(a)
            f_rec(a+1, b)
    else:
        if a == b:
            print(a)
        else:
            print(a)
            f_rec(a-1, b)


f(1, 5)
print("---")
f(5, 1)
print("---")
f_rec(1, 5)
print("---")
f_rec(5, 1)
