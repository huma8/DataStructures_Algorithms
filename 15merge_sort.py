""" 
birleştirme sıralaması algoritması uygulaması.
Bu algoritma, bir diziyi sıralamak için böl ve fethet yaklaşımını kullanır.
Algoritma, diziyi daha küçük alt dizilere böler, bu alt dizileri sıralar ve ardından sıralanmış alt dizileri birleştirir.
O(n log n) zaman karmaşıklığına sahiptir.

bakınız:
references\\merge_sort.png, references\\merge_sort2.png
"""
def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    lindex, rindex = 0, 0
    while lindex < len(left) and rindex < len(right):
        if left[lindex] <= right[rindex]:
            sorted_array.append(left[lindex])
            lindex += 1
        else:
            sorted_array.append(right[rindex])
            rindex += 1
    sorted_array.extend(left[lindex:])
    sorted_array.extend(right[rindex:])
    return sorted_array

array = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(array))