import time
import random
import matplotlib.pyplot as plt

import sort.BubleSort as BubleSort
import sort.QuickSort as QuickSort
import sort.SelectionSort as SelectionSort

COUNTS = [10, 100, 1_000, 10_000]

buble = [[], [], [], []]
quick = [[], [], [], []]
selection = [[], [], [], []]

for n in COUNTS:
    origin = [random.randint(0, 100) for _ in range(n)]
    print(f"{n} ЭЛЕМЕНТОВ:")

    buble[0].append(n)
    quick[0].append(n)
    selection[0].append(n)

    start_time = time.time()
    _, count_permutations, count_comparisons = BubleSort.buble_sort(origin)
    end_time = time.time()
    delta_time = end_time - start_time
    buble[1].append(delta_time)
    buble[2].append(count_permutations)
    buble[3].append(count_comparisons)
    print(f"- Пузырьковая сортировка\n- Кол-во перестановок: {count_permutations}\n- Кол-во сравнений: {count_comparisons}\n- Время выполнения: {delta_time}\n")

    start_time = time.time()
    _, count_permutations, count_comparisons = QuickSort.quick_sort(origin, 0, 0)
    end_time = time.time()
    delta_time = end_time - start_time
    quick[1].append(delta_time)
    quick[2].append(count_permutations)
    quick[3].append(count_comparisons)
    print(f"- Быстрая сортировка\n- Кол-во перестановок: {count_permutations}\n- Кол-во сравнений: {count_comparisons}\n- Время выполнения: {delta_time}\n")

    start_time = time.time()
    _, count_permutations, count_comparisons = SelectionSort.selection_sort(origin)
    end_time = time.time()
    delta_time = end_time - start_time
    selection[1].append(delta_time)
    selection[2].append(count_permutations)
    selection[3].append(count_comparisons)
    print(f"- Сортировка выбором\n- Кол-во перестановок: {count_permutations}\n- Кол-во сравнений: {count_comparisons}\n- Время выполнения: {delta_time}")

    print("---------------------")

fig, axs = plt.subplots(1, 3, figsize=(10, 6))

axs[0].set_title('Рост времени\nс увеличением кол-ва элементов')
axs[0].plot(buble[0], buble[1], label='Пузырьковая сортировка')
axs[0].plot(quick[0], quick[1], label='Быстрая сортировка')
axs[0].plot(selection[0], selection[1], label='Сортировка выбором')
axs[0].scatter(buble[0], buble[1], color='blue')
axs[0].scatter(quick[0], quick[1], color='blue')
axs[0].scatter(selection[0], selection[1], color='blue')
axs[0].set_yticks(list(set(buble[1] + quick[1] + selection[1])))
axs[0].set_ylabel('Время, сек.')
axs[0].tick_params(axis='y', labelsize=8)

axs[1].set_title('Рост кол-ва сравнений в зависимсоти\nот алгоритма и кол-ва элементов')
axs[1].plot(buble[0], buble[2], label='Пузырьковая сортировка')
axs[1].plot(quick[0], quick[2], label='Быстрая сортировка')
axs[1].plot(selection[0], selection[2], label='Сортировка выбором')
axs[1].scatter(buble[0], buble[2], color='blue')
axs[1].scatter(quick[0], quick[2], color='blue')
axs[1].scatter(selection[0], selection[2], color='blue')
axs[1].set_yticks(list(set(buble[3] + quick[3] + selection[3])))
axs[1].set_ylabel('Кол-во сравнений, шт.')
axs[1].tick_params(axis='y', labelsize=8)

axs[2].set_title('Рост кол-ва перестановок в зависимсоти\nот алгоритма и кол-ва элементов')
axs[2].plot(buble[0], buble[3], label='Пузырьковая сортировка')
axs[2].plot(quick[0], quick[3], label='Быстрая сортировка')
axs[2].plot(selection[0], selection[3], label='Сортировка выбором')
axs[2].scatter(buble[0], buble[3], color='blue')
axs[2].scatter(quick[0], quick[3], color='blue')
axs[2].scatter(selection[0], selection[3], color='blue')
axs[2].set_yticks(list(set(buble[2] + quick[2] + selection[2])))
axs[2].set_ylabel('Кол-во перестановок, шт.')
axs[2].tick_params(axis='y', labelsize=8)

for ax in fig.get_axes():
    ax.label_outer()

for ax in axs:
    ax.set_xlabel('Кол-во элементов, шт.')
    ax.legend()
    ax.set_xticks(COUNTS)

plt.tight_layout()
plt.show()
