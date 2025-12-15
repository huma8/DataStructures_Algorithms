"""Depth First Search (DFS) Algoritması
DFS, bir graf veya ağaç veri yapısında derinlemesine arama yapmak için kullanılan bir algoritmadır.
DFS, başlangıç düğümünden başlayarak mümkün olduğunca derinlemesine ilerler ve ardından geri dönerek diğer yolları keşfeder.
DFS, genellikle yığın (stack) veri yapısı kullanılarak uygulanır ve hem
özyinelemeli (recursive) hem de iteratif (iterative) yöntemlerle gerçekleştirilebilir.
DFS, labirent çözme, yol bulma ve bağlantılı bileşenleri keşfetme gibi çeşitli uygulamalarda kullanılır.

bakınız:
references\depth_first.png
references\depth_first2.png
references\depth_first3.png
references\depth_first4.png
"""

class Graph:
    def __init__(self, size):
        self.size = size
        self.graph_list = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, src, dst):
        self.graph_list[src][dst] = 1 #directed list.

    def remove_edge(self, src, dst):
        self.graph_list[src][dst] = 0

    def is_edge(self, u, v) -> bool:
        return self.graph_list[u][v] == 1

    def display_matrix(self):
        for i in self.graph_list:
            for j in i:
                print(f"{j}", end=" ")
            print()

    def depth_first_search(self, src, visited_nodes):
        if visited_nodes[src]:
            return
        else:
            visited_nodes[src] = True
            print(src, end=" ")  # Print the visited node

        for i in range(self.size):  # Iterate through the range of size, not self.size directly
            if self.graph_list[src][i] == 1:
                self.depth_first_search(i, visited_nodes)
        return

graph = Graph(5)
graph.add_edge(0, 1)

graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 3)
graph.add_edge(0, 3)
graph.add_edge(0, 3)

graph.add_edge(2, 1)
graph.add_edge(2, 0)
graph.add_edge(3, 0)
graph.add_edge(3, 0)
graph.add_edge(3, 1)

graph.add_edge(2, 3)
graph.add_edge(3, 2)
graph.add_edge(3, 3)


print(graph.graph_list)
print("Matrix: \n")
graph.display_matrix()
print("\nDepth_first_search: \n")
visited_nodes = [False] * graph.size
graph.depth_first_search(0, visited_nodes)
print("Farkettiğin üzere 4 yazılmadı çünkü hiçbir edge 4 e uğramadı veya 4 ten çıkmadı.")  # For a newline after DFS output

"""
EXAMPLE
# Labirent benzeri kullanım örneği: Bir düğümden diğerine yol bulma
def dfs_find_path(graph, current, target, visited, path):
    visited[current] = True
    path.append(current)

    if current == target:
        return True  # Hedefe ulaşıldı

    # Komşuları kontrol et
    for neighbor in range(graph.size):
        if graph.graph_list[current][neighbor] == 1 and not visited[neighbor]:
            if dfs_find_path(graph, neighbor, target, visited, path):
                return True

    # Geriye doğru izleme (backtrack)
    path.pop()
    return False

print("\nLabirent benzeri örnek - Düğüm 0'dan 4'e giden yol:")
path = []
visited = [False] * graph.size
if dfs_find_path(graph, 0, 4, visited, path):
    print(f"Bulunan yol: {' -> '.join(map(str, path))}")
else:
    print("Yol bulunamadı")
"""