import time
import random
import matplotlib.pyplot as plt
import sort.BubleSort as BubleSort
import sort.QuickSort as QuickSort
import sort.SelectionSort as SelectionSort

COUNTS = [10, 100, 1_000, 10_000]

buble = [[], []]
quick = [[], []]
selection = [[], []]

for n in COUNTS:
    origin = [random.randint(0, 100) for _ in range(n)]

    buble[0].append(n)
    quick[0].append(n)
    selection[0].append(n)

    start_time = time.time()
    BubleSort.buble_sort(origin)
    end_time = time.time()
    buble[1].append(end_time - start_time)

    start_time = time.time()
    QuickSort.quick_sort(origin)
    end_time = time.time()
    quick[1].append(end_time - start_time)

    start_time = time.time()
    SelectionSort.selection_sort(origin)
    end_time = time.time()
    selection[1].append(end_time - start_time)

    print(f'Массив длины {n} отсортирован')

plt.xlabel('Кол-во элементов, шт.', color='blue')
plt.ylabel('Время, с.', color='green')
plt.title('Рост времени с увеличением кол-ва элементов')

plt.plot(buble[0], buble[1], label='Пузырьковая сортировка')
plt.plot(quick[0], quick[1], label='Быстрая сортировка')
plt.plot(selection[0], selection[1], label='Сортировка выбором')

plt.scatter(buble[0], buble[1], color='blue')
plt.scatter(quick[0], quick[1], color='blue')
plt.scatter(selection[0], selection[1], color='blue')

plt.xticks(COUNTS, [n for n in COUNTS])

plt.legend()
plt.show()
