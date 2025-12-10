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
        self.array
        pass

    def delete(self):
        pass

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

    def search(self, index):
        if 0 <= index < self.n:
            return self.array[index]
        raise IndexError("index out of bounds")

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
