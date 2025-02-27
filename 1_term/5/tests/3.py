data = ([1, 4], [4, 3], [3, 5], [2, 6], [2, 8])
n = int(input())

output = []

for el in data:
    el.append(n)
    output.append(el)

print(tuple(output))
