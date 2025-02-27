import time
import random
import matplotlib.pyplot as plt
import sort.BubleSort as BubleSort
import sort.QuickSort as QuickSort
import sort.SelectionSort as SelectionSort

COUNTS = [10, 100, 1_000, 10_000]

buble_x = []
buble_y = []

quick_x = []
quick_y = []

selection_x = []
selection_y = []

for n in COUNTS:
    origin = [random.randint(0, 100) for _ in range(n)]

    buble_x.append(n)
    quick_x.append(n)
    selection_x.append(n)

    start_time = time.time()
    BubleSort.buble_sort(origin)
    end_time = time.time()
    buble_y.append(end_time - start_time)

    start_time = time.time()
    QuickSort.quick_sort(origin)
    end_time = time.time()
    quick_y.append(end_time - start_time)

    start_time = time.time()
    SelectionSort.selection_sort(origin)
    end_time = time.time()
    selection_y.append(end_time - start_time)

    print(f'Массив длины {n} отсортирован')

plt.xlabel('Кол-во элементов, шт.', color='blue')
plt.ylabel('Время, с.', color='green')
plt.title('Рост времени с увеличением кол-ва элементов')

plt.plot(buble_x, buble_y, label='Пузырьковая сортировка')
plt.plot(quick_x, quick_y, label='Быстрая сортировка')
plt.plot(selection_x, selection_y, label='Сортировка выбором')

plt.legend()
plt.show()
