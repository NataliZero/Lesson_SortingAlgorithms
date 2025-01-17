def bubble_sort(arr):
    n = len(arr)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Пример использования
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", numbers)
    bubble_sort(numbers)
    print("Отсортированный массив:", numbers)
