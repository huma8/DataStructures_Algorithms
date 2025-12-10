"""
Elementleri tek tek inceleyerek arama yapan basit bir algoritma.

O(n) zaman karmaşıklığına sahiptir. 
Sıralanmamış listelerde kullanılır. 
İndeksi olmayan verilerde kullanışlıdır. 
Küçük veya orta büyüklükteki veri setlerinde etkilidir. Büyük veri setlerinde yavaş olabilir.
"""

array = [3, 5, 2, 4, 9, 1, 8, 7, 6]

def linear_search(arr, target) -> int | str:
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return "Not Found"

target_value = 6
result_index = linear_search(array, target_value)
print(result_index)