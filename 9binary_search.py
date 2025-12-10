"""
Çalışması için sıralanmış bir liste gerektiren ikili arama algoritmasını uygular.
"""
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Hedef değeri bulduk
        if arr[mid] == target:
            return mid
        # Hedef değer orta değerden büyükse, sağ yarıda aramaya devam et
        elif arr[mid] < target:
            left = mid + 1
        # Hedef değer orta değerden küçükse, sol yarıda aramaya devam et
        else:
            right = mid - 1

    # Hedef değer bulunamadı
    return -1