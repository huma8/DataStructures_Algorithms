"""
Ağaç Veri Yapıları
Ağaç veri yapıları, düğümler (nodes) ve kenarlardan (edges) oluşan hiyerarşik bir yapıyı temsil eder. 
Her düğüm, bir veri öğesi içerir ve diğer düğümlere bağlantılar (kenarlar) aracılığıyla bağlanır. 
Ağaçlar, kök düğüm (root node) adı verilen tek bir başlangıç düğümüne sahiptir ve her düğümün sıfır 
veya daha fazla alt düğümü (child nodes) olabilir.

Ağaç veri yapılarının temel özellikleri şunlardır:
1. Kök Düğüm (Root Node): Ağacın en üstündeki düğümdür ve tüm diğer düğümler buradan dallanır.
2. Yaprak Düğümler (Leaf Nodes): Alt düğümü olmayan düğümlerdir.
3. Düğüm Derecesi (Node Degree): Bir düğümün sahip olduğu alt düğüm sayısıdır.
4. Yükseklik (Height): Ağacın kök düğümünden en derin yaprak düğüme kadar olan en uzun yolun uzunluğudur.
5. Alt Ağaç (Subtree): Bir düğüm ve onun tüm alt düğümlerinden oluşan ağaçtır.
6. Boyut (Size): Ağacın içindeki toplam düğüm sayısıdır.
7. Derinlik (Depth): Bir düğümün kök düğümden olan uzaklığıdır.


Ağaç veri yapıları, birçok farklı türde olabilir, örneğin:
- İkili Ağaç (Binary Tree): Her düğümün en fazla iki alt düğüme sahip olduğu ağaç türüdür.
- İkili Arama Ağacı (Binary Search Tree): İkili ağaçların özel bir türüdür; sol alt düğümler, ebeveyn düğümden 
    daha küçük değerler içerirken, sağ alt düğümler daha büyük değerler içerir.



bakınız:
references\\tree_ds.png
"""

