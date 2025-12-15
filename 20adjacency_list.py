"""
Adjacency List:
An adjacency list is a collection of lists or arrays used to represent a graph.
Each vertex has a list of all the vertices it is connected to.

time complexity: O(V)
space complexity: O(V + E)

bakınız:
references\\graphs-list.png
references\\adjacent_list.png
"""

class adjacencyList:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v) # For directed graph

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v) # For directed graph

    def is_edge(self, u, v):
        return v in self.adj_list[u]

    def display(self):
        for i in range(self.V):
            print(f"{i}:", end="-> ")
            for j in self.adj_list[i]:
                print(f"{j}", end=" -> ")
            print()
        
graph = adjacencyList(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)

graph.add_edge(0, 3) #directed edge
graph.add_edge(3, 0) #directed edge

graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.remove_edge(1, 2)
graph.display()
print(graph.is_edge(1, 0))  # False
print(graph.is_edge(2, 3))  # True

