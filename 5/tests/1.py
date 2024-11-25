from random import randint

arr1 = [randint(1, 10) for _ in range(5)]
arr2 = [randint(1, 10) for _ in range(5)]

print(arr1)
print(arr2)

output = []

for n in arr1:
    if n in arr2 and n not in output:
        output.append(n)

print(output)
