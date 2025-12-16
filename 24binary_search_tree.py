"""
Binary Search Tree (BST) Nedir?
Binary Search Tree (BST), her düğümün en fazla iki çocuğa sahip olduğu ve sol alt ağacındaki tüm düğümlerin değerlerinin 
ebeveyn düğümün değerinden küçük, sağ alt ağacındaki tüm düğümlerin değerlerinin ise ebeveyn düğümün değerinden büyük 
olduğu bir veri yapısıdır. Bu özellik, arama, ekleme ve silme işlemlerinin verimli bir şekilde gerçekleştirilmesini sağlar.

O(log n) zaman karışılığına sahiptir.


bakınız:
references\\tree_ds.png
references\\tree_ds2.png
references\\tree_ds3.png
references\\tree_ds4.png
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search_rec(node.left, key)
        return self._search_rec(node.right, key)
    
    def inorder(self):
        return self._inorder_rec(self.root)
    
    def _inorder_rec(self, node):
        return self._inorder_rec(node.left) + [node.val] + self._inorder_rec(node.right) if node else []
    
bstree = BST()
bstree.insert(50)
bstree.insert(30)
bstree.insert(20)
bstree.insert(40)
bstree.insert(70)
bstree.insert(60)
bstree.insert(80)
print("Inorder traversal of the BST:", bstree.inorder())
result = bstree.search(40)
if result:
    print("Found:", result.val)
else:
    print("Not Found")