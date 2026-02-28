import random

# 1. Заполняем массивы вручную через while
arr1 = [0] * 50
arr2 = [0] * 50

i = 0
while i < 50:
    arr1[i] = random.randint(0, 100)
    arr2[i] = random.randint(0, 100)
    i += 1

# 2. Сортируем первый массив (без этого бинарный поиск не работает)
# Используем классический "Пузырек" через while
i = 0
while i < 50:
    j = 0
    while j < 49 - i:
        if arr1[j] > arr1[j + 1]:
            # Меняем местами
            temp = arr1[j]
            arr1[j] = arr1[j + 1]
            arr1[j + 1] = temp
        j += 1
    i += 1

print("Отсортированный массив 1: ", arr1)
print("Массив 2: ", arr2)

# 3. Реализация Бинарного поиска (тот самый "Бинарный метод")
def binary_search(array, target):
    low = 0
    high = 49 # так как длина 50, последний индекс 49
    
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return True # Нашли!
        elif array[mid] < target:
            low = mid + 1 # Ищем в правой части
        else:
            high = mid - 1 # Ищем в левой части
    return False # Не нашли

# 4. Ищем повторяющиеся элементы
duplicates = []
i = 0
while i < 50:
    current_number = arr2[i]
    
    # Используем наш бинарный метод для поиска числа из arr2 в arr1
    if binary_search(arr1, current_number):
        
        # Проверка на уникальность в списке результатов, 
        # чтобы одно и то же число не вывелось дважды
        already_in_results = False
        k = 0
        while k < len(duplicates):
            if duplicates[k] == current_number:
                already_in_results = True
            k += 1
            
        if not already_in_results:
            duplicates.append(current_number)
    i += 1

print("-" * 30)
print("Найденные повторения (бинарным методом):")
print(duplicates)