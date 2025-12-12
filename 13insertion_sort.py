import random, time

"""Insertion Sort Implementation with Timing
insert metodu ile verilen diziyi sıralar ve işlem süresini ölçer.
O(n^2) zaman karmaşıklığına sahiptir.
küçük veri setleri için uygundur.
büyük veri setleri için önerilmez.
bubble_sorttan daha hızlıdır.
selection_sorttan daha yavaştır(ya da nadiren aynı).

"""

def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > tmp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    end_time = time.time()
    print(f"Insertion Sort took {end_time - start_time:.6f} seconds")
    return arr


array = [random.randint(0, 1000) for _ in range(1000)]
print(insertion_sort(array)[::10])