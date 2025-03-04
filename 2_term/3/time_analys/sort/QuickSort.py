def quick_sort(arr, count_permutations, count_comparisons):
    if len(arr) <= 1:
        return arr, count_permutations, count_comparisons

    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
        count_permutations += 1
        count_comparisons += 1

    return quick_sort(left, count_permutations, count_comparisons)[0] + [pivot] + quick_sort(right, count_permutations, count_comparisons)[0], count_permutations, count_comparisons
