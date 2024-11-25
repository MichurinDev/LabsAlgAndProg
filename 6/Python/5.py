# Разработайте функцию, которая принимает список чисел в качестве аргумента. 
# Она должна вычислить количество этих чисел, сумму всех чисел в списке и 
# вернуть это значение.

def f(l: list) -> tuple:
    count, sum_nums = 0, 0

    for i in l:
        count += 1
        sum_nums += i
    
    return count, sum_nums


def f_rec(l: list):
    if not l:
        return 0, 0
    
    count, sum_nums = f_rec(l[1:])
    count += 1
    sum_nums += l[0]

    return count, sum_nums

arr = [1, 2, 3, 4, 5]

print(f(arr))
print("---")
print(f_rec(arr))
