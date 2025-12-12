import time, random
"""
Bubble Sort Algorithm Uygulaması
Bu işlev, kabarcık sıralama algoritmasını kullanarak bir diziyi sıralar.
Ayrıca, sıralama işlemi sırasında geçen süreyi ve yapılan değişimlerin (denemelerin) sayısını ölçer.

Ortalama ve en kötü durumda O(n^2) zaman karmaşıklığı.
Küçük veri setleri için uygundur. Büyük veri setleri için önerilmez.
"""

def bubble_sort(arr):
    tries = 0
    n = len(arr)
    # Traverse through all array elements
    start_time = time.time()
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                tries += 1
    end_time = time.time()
    print(f"Bubble Sort took {end_time - start_time:.6f} seconds and {tries} tries.")
    return arr

random_array = [random.randint(0, 1000) for _ in range(1000)]
print(bubble_sort(random_array)[::100])