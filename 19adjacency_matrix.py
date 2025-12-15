"""
Adjacency Matrix:
An adjacency matrix is a 2D array of size V x V where V is the number of vertices in a graph.
Each cell in the matrix represents whether there is an edge between two vertices.

time complexity: O(1)
space complexity: O(V^2)

bakınız:
references\graphs-matrix.png
references\\adjacent_matrix.png
"""

class AdjacencyMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1  # For undirected graph

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0  # For undirected graph

    def is_edge(self, u, v):
        return self.adj_matrix[u][v] == 1

    def display(self):
        for i in self.adj_matrix:
            for j in i:
                print(f"{j}", end=" ")
            print()

matrix = AdjacencyMatrix(4)
matrix.add_edge(0, 1)
matrix.add_edge(0, 2)
matrix.add_edge(1, 2)
matrix.add_edge(2, 3)
matrix.remove_edge(0, 2)
matrix.display()
print(matrix.is_edge(1, 0))  # True [u][v] = [v][u]
print(matrix.is_edge(2, 2))  # False
