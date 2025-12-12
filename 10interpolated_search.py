"""
Uniform dağılmış, sıralanmış bir listede hesaplanmış sonda araması algoritmasını uygular.
Eğer arama başarısız olursa arama alanı daraltılır. Yeni tahmin, hedef değerin
değerine göre hesaplanır.

Eğer dizi üniform değilse, algoritmanın performansı düşer.

ortalama zaman karmaşıklığı: O(log log n)
en kötü zaman karmaşıklığı: O(n)
"""
def interpolated_search(arr, target):
    left, right = 0, len(arr) - 1
    count_try = 0

    while left <= right and target >= arr[left] and target <= arr[right]:
        # Hedef değerin konumunu tahmin et
        pos = left + ((target - arr[left]) * (right - left) // (arr[right] - arr[left]))
        count_try += 1
        # Hedef değeri bulduk
        if arr[pos] == target:
            return pos, count_try
        # Hedef değer tahmin edilen değerden büyükse, sağ yarıda aramaya devam et
        elif arr[pos] < target:
            left = pos + 1
        # Hedef değer tahmin edilen değerden küçükse, sol yarıda aramaya devam et
        else:
            right = pos - 1

    # Hedef değer bulunamadı
    return -1, count_try

basic_array = [10, 20, 30, 40, 50]
mid_time_array = [i for i in range(0, 1000000, 10)]
worst_time_array = [i for i in range(0, 1000000)]

# Call the function once and store both return values
index1, tries1 = interpolated_search(basic_array, 30)  # Changed to 30 for basic array to see more tries
index2, tries2 = interpolated_search(mid_time_array, 500000)  # Searching for middle element
index3, tries3 = interpolated_search(worst_time_array, 500000)  # Searching for middle element

print(f"\nBasic: {index1}, \nDeneme sayısı: {tries1}\n")
print(f"Mid Time: {index2}, \nDeneme sayısı: {tries2}\n")
print(f"Worst Time: {index3}, \nDeneme sayısı: {tries3}\n")

# Additional example with a non-uniform array to better show multiple tries
non_uniform_array = [1, 2, 3, 10, 20, 30, 100, 200, 300, 1000, 2000, 3000, 10000, 20000, 30000]
index4, tries4 = interpolated_search(non_uniform_array, 200)
print(f"Non-uniform Array: {index4}, \nDeneme sayısı: {tries4}\n")
