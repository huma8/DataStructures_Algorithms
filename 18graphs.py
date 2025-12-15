""" A graph is aggregated as a set of nodes(vertex) and edges like facebook. 

Undirected graph is used to represent friendships in facebook.
Each node represents a user, and each edge represents a friendship between two users.
a user has a adjacency(yakınlık) list to represent all his friends.

Directed graph is used to represent followers in twitter.
Each node represents a user, and each directed edge represents a follower relationship between two users.
Ben birini takip ediyor olabilirim ama o kişi beni takip etmeyebilir.(directed yani yönlü)

------------------------------------------------------------------------------------------------------------------
Adjacency Matrix:
An adjacency matrix is a 2D array of size V x V where V is the number of vertices in a graph.
Each cell in the matrix represents whether there is an edge between two vertices.

time complexity: O(1)
space complexity: O(V^2)

bakınız:
references\graphs-matrix.png

------------------------------------------------------------------------------------------------------------------
Adjacency List:
An adjacency list is a collection of lists or arrays used to represent a graph.
Each vertex has a list of all the vertices it is connected to.

time complexity: O(V)
space complexity: O(V + E)

bakınız:
references\graphs-list.png
"""


