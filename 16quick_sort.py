"""Quick Sort Implementation
Hızlı sıralama metodu kullanılarak bir diziyi sıralar.
en iyi durum: O(n log n)
ortalama durum: O(n log n)
en kötü durum: O(n^2). eğer dizi zaten sıralıysa.
bakınız:
references\\quick_sort.png
"""
import random


def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

array = [random.randint(0, 10000) for _ in range(100000)]
print(quick_sort(array)[::1000])