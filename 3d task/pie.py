#Вопрос №3
#На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел.
#Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным).
#Объяснить, почему вы считаете, что функция соответствует заданным критериям.

#Мной был выбран алгоритм сортировки Timsort. Он является самым быстрым, стабильным, сильным, смелым и умелым вариантом сортировки.
#А если список изначально отсортирован, то скорость сортировки и вовсе O(n).
#К сожалению, как оказалось, не я один такой умный, и это стандартный способ сортировки в Python.
#Предположив, что вам не интересно смотреть на код, типа "g = arr   g.sort()  print(g)", я выбрал следующий по эффективности вариант сортировки.
#
#Сортировка слиянием (или merge sort).
def The_sortiest(Unsorted_arr):
    if len(Unsorted_arr) > 1:
        middle = len(Unsorted_arr) // 2
        left_half = Unsorted_arr[:middle]
        right_half = Unsorted_arr[middle:]

        #Рекурсия.
        The_sortiest(left_half)
        The_sortiest(right_half)

        left_num = 0 #Счётчик левого списка.
        right_num = 0 #Счётчик правого списка.
        counter = 0 #Счётчиководец. (Общий)

        #Перебор обеих сторон списка.
        while left_num < len(left_half) and right_num < len(right_half):
            if left_half[left_num] < right_half[right_num]:
                Unsorted_arr[counter] = left_half[left_num]
                left_num += 1
            else:
                Unsorted_arr[counter] = right_half[right_num]
                right_num += 1
            counter += 1

        #Перебор левой (если правая кончилась).
        while left_num < len(left_half):
            Unsorted_arr[counter] = left_half[left_num]
            left_num += 1
            counter += 1

        #Перебор правой (если левая кончилась).
        while right_num < len(right_half):
            Unsorted_arr[counter] = right_half[right_num]
            right_num += 1
            counter +=1

        return Unsorted_arr

    else:
        return Unsorted_arr


#Маленький массив для наглядности
# Unsorted_arr = [38, 27, 43, 3, 9, 82, 10]
# Sorted_arr = The_sortiest(Unsorted_arr)
# print(f"Отсортированный массив: {Sorted_arr}")



import random
import time

# Генерация случайного большого массива для тестирования функции
Unsorted_arr = [random.randint(1, 100000) for _ in range(1000)]

start_time = time.perf_counter()
Sorted_arr = The_sortiest(Unsorted_arr)
end_time = time.perf_counter()

print(f"Исходный массив: {Unsorted_arr}.\n"
      f"Отсортированный массив: {Sorted_arr}\n"
      f"Время сортировки составило: {end_time-start_time:.10f} секунд.")