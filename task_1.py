import random
import time
import matplotlib.pyplot as plt
import sys

# Збільшуємо ліміт рекурсії, щоб уникнути помилки при сортуванні дуже великих масивів
sys.setrecursionlimit(10**7)

def randomized_quick_sort(arr):
    """
    Рандомізований QuickSort.
    Опорний елемент (pivot) обирається випадковим чином.
    Використовується нерекурсивний підхід "розділяй та володарюй" (розділення + рекурсія).
    """
    # Якщо масив має менше двох елементів, він вже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на три частини: менші за pivot, рівні pivot та більші за pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

def measure_time(sort_func, arr, repeats=5):
    """
    Функція для вимірювання середнього часу виконання алгоритму сортування.
    sort_func: функція сортування (randomized_quick_sort або deterministic_quick_sort)
    arr: масив, який потрібно сортувати
    repeats: кількість повторів для усереднення часу
    """
    total_time = 0
    for _ in range(repeats):
        arr_copy = arr[:]  # Копіюємо масив, щоб не сортувати той самий "зіпсований" після першого сортування
        start = time.time()
        sort_func(arr_copy)
        end = time.time()
        total_time += (end - start)
    return total_time / repeats

def main():
    # Розміри масивів для тестування
    sizes = [10000, 50000, 100000, 500000]

    # Списки для збереження результатів часу
    times_random = []
    times_det = []

    # Перебираємо кожен розмір масиву
    for size in sizes:
        # Генеруємо масив випадкових цілих чисел
        arr = [random.randint(0, 10**6) for _ in range(size)]

        # Вимірюємо час для рандомізованого QuickSort
        avg_time_random = measure_time(randomized_quick_sort, arr)
        # Вимірюємо час для детермінованого QuickSort
        avg_time_det = measure_time(deterministic_quick_sort, arr)

        # Зберігаємо результати у списки
        times_random.append(avg_time_random)
        times_det.append(avg_time_det)

        # Виводимо результати у консоль (у форматі, наведеному в завданні)
        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {avg_time_random:.4f} секунд")
        print(f"   Детермінований QuickSort: {avg_time_det:.4f} секунд\n")

    # Побудова графіка порівняння
    plt.plot(sizes, times_random, label='Рандомізований QuickSort')
    plt.plot(sizes, times_det, label='Детермінований QuickSort')
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунд)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
