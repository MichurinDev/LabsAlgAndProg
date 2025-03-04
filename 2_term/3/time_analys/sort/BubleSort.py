def buble_sort(arr):
    count_permutations, count_comparisons = 0, 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count_permutations += 1
            count_comparisons += 1

    return arr, count_permutations, count_comparisons
