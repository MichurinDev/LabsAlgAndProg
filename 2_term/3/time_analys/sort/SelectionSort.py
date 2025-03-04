def selection_sort(arr):
    count_permutations, count_comparisons = 0, 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
            count_comparisons += 1

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        count_permutations += 1

    return arr, count_permutations, count_comparisons
