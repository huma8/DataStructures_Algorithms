from heapq import __all__, heappush, heappop
heap = []
print(f"{__all__}\nUsable functions are above.")

heappush(heap,10)
heappush(heap,20)
heappush(heap,5)
heappush(heap,90)
print(f"{heap}")
heappop(heap)
print(f"Kalanlar = {heap}")
