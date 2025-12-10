#index + data + location(dizinin büyüklüğü + dizinin kapasitesi)    bilgilerini barındırır.
#ARTILARI= hızlı erişim, hızlı insert/remove element, iyi lokalizasyon ve veri önbelleği kullanımı.
#EKSİLERİ= fazla hafıza kullanımı. shifting, dizi büyütme, dizi küçültme zaman gerektirir,


import ctypes

class DynamicArray:
    def __init__(self):
        self.n = 0                      # Eleman sayısı
        self.capacity = 1               # Başlangıç kapasitesi
        self.array = self._make_array(self.capacity)

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def add(self, item):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.n] = item
        self.n += 1

    def insert(self, index, data):
        if not 0 <= index <= self.n:
            raise IndexError("index out of bounds")
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        for i in range(self.n, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = data
        self.n += 1

    def delete(self, data=None):
        if self.n == 0:
            raise IndexError("delete from empty array")
        if data is not None:
            for i in range(self.n):
                if self.array[i] == data:
                    for j in range(i, self.n - 1):
                        self.array[j] = self.array[j + 1]
                    self.array[self.n - 1] = None
                    self.n -= 1
                    if 0 < self.n < self.capacity // 4:
                        self._resize(self.capacity // 2)
                    return
            raise ValueError("value not found in array")
        else:
            self.array[self.n - 1] = None
        self.n -= 1
        if 0 < self.n < self.capacity // 4:
            self._resize(self.capacity // 2)

    def _make_string(self) -> str:
        string = ""
        for i in range(self.n):
            string += self.array[i] + ","
        return string

    def _resize(self, new_capacity):
        new_array = self._make_array(new_capacity)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def search(self, data):
        if type(data) is not str:
            if 0 <= data < self.n:
                return self.array[data]
            raise IndexError("index out of bounds")
        elif type(data) is str:
            for i in range(self.n):
                if self.array[i] == data:
                    return i
            return -1

    def __len__(self):
        return self.n

    def _is_empty(self):
        return self.n == 0

dynarr = DynamicArray()

dynarr.add("Ali")
dynarr.add("veli")
dynarr.add("zeki")
dynarr.add("ulvi")
print(dynarr._make_string())
print(dynarr._is_empty())
dynarr.insert(0, "ahmet")
dynarr.delete("veli")
print(dynarr._make_string())
print(dynarr.search("ulvi"))
