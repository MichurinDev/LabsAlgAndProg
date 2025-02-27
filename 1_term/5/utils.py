def lenght(string: str) -> int:
    counter = 0
    for _ in string:
        counter += 1
    return counter


def sort_tuples(tuples, n):
    data = list(tuples)
    n -= 1

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i][n] > data[j][n]:
                data[i], data[j] = data[j], data[i]

    return tuple(data)


def count(l, el):
    c = 0
    for i in l:
        if i == el:
            c += 1
    return c
