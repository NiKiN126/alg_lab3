import random
import time


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


n = int(input("Введите количество элементов в массиве: "))

arr = random.sample(range(-5000, 5000), n)

print("Сгенерированный массив:", arr)

target_element = int(input("Введите элемент для поиска: "))

start_time = time.time()

result = linear_search(arr, target_element)

end_time = time.time()
elapsed_time = end_time - start_time

if result != -1:
    print(f"Элемент {target_element} найден в массиве. Индекс: {result}")
else:
    print(f"Элемент {target_element} не найден в массиве.")

print(f"Время выполнения: {elapsed_time} секунд")
