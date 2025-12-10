#FIFO(First in, First out) -> Listeye ilk giren, ilk çıkar.
#Nerede Kullanılır?
#klavyeyle veri girerken. Yazdırma işlerinde(sıraya göre). LinkedList, PriorityQueues, Breadth-first search

from collections import deque

class QueueDeque:
    def __init__(self):
        self._d = deque()

    def enqueue(self, value):
        """Sona ekle (enqueue)"""
        self._d.append(value)

    def dequeue(self):
        """Baştan çıkar (dequeue). Boşsa IndexError fırlatır."""
        if not self._d:
            raise IndexError("dequeue from empty queue")
        return self._d.popleft()

    def peek(self):
        """Ön elemanı döndür (None veya hata tercih edilebilir)."""
        return self._d[0] if self._d else None

    def is_empty(self):
        return not self._d

    def size(self):
        return len(self._d)

queue = QueueDeque()
queue.enqueue("ali")
queue.enqueue("veli")
queue.enqueue("ahmet")
queue.enqueue("mehmet")
print(queue._d)
print(queue.peek())
queue.dequeue()
queue.dequeue()
print(queue.size())
print(queue.is_empty())
