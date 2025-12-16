"""
Breadth-First Search (BFS) Algoritması
Breadth-First Search (BFS), bir graf veya ağaç veri yapısında en kısa yolu bulmak için kullanılan yaygın bir arama algoritmasıdır.
BFS, başlangıç düğümünden başlayarak tüm komşu düğümleri keşfeder ve ardından bu komşuların komşularını keşfetmeye devam eder.
Bu süreç, hedef düğüme ulaşılana kadar devam eder.

BFS algoritması, genellikle kuyruk (queue) veri yapısı kullanılarak uygulanır. 
Kuyruk, keşfedilecek düğümlerin sırasını tutar ve FIFO (First In, First Out) prensibine göre çalışır.



bakınız:
references\\breadth_first_search_step1.png
references\\breadth_first_search_step2.png
references\\breadth_first_search_step3.png
references\\breadth_first_search.png
"""
from collections import deque

def bfs(graph, start, goal):
    # Başlangıç düğümünü kuyruğa ekle
    queue = deque([start])
    # Ziyaret edilen düğümleri takip etmek için bir küme oluştur
    visited = set()
    visited.add(start)
    # Her düğümün önceki düğümünü takip etmek için bir sözlük oluştur
    parent = {start: None}

    while queue:
        # Kuyruğun önünden bir düğüm çıkar
        current = queue.popleft()

        # Hedef düğüme ulaşıldıysa, yolu geri izleyerek döndür
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Ters çevirerek doğru sırada döndür

        # Mevcut düğümün tüm komşularını keşfet
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    return None  # Hedef düğüme ulaşılamadıysa None döndür

print("Breadth-First Search (BFS) Algoritması")
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D', 'E', 'G'],
    'C': ['A', 'F', 'H'],
    'D': ['A', 'B', 'E', 'I'],
    'E': ['B', 'D', 'F', 'J'],
    'F': ['C', 'E', 'G', 'K'],
    'G': ['B', 'F', 'H', 'L'],
    'H': ['C', 'G', 'I'],
    'I': ['D', 'H', 'J'],
    'J': ['E', 'I', 'K'],
    'K': ['F', 'J', 'L'],
    'L': ['G', 'K']
}

print(bfs(graph, 'A', 'L'))