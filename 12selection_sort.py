import time, random

"""Selection Sort Algorithm with Time Measurement
Bu modül, seçim sıralama algoritmasını uygular ve yürütme süresini ölçer.
O(n^2) zaman karmaşıklığı.
Küçük veri kümeleri için uygundur.
Büyük veri kümeleri için uygun değildir.
"""

def selection_sort(array) -> list:
    n = len(array)
    start_time = time.time()
    for i in range(n):
        minx = i
        for j in range(i + 1, n):
            if array[j] < array[minx]:
                minx = j
        array[i], array[minx] = array[minx], array[i]
    end_time = time.time()
    print(f"Selection Sort took {end_time - start_time:.6f} seconds")
    return array

array = [random.randint(0, 1000) for _ in range(1000)]
print(selection_sort(array)[::100])