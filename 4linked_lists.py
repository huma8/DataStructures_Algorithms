#arraylist i düşün array = ["a", "l", "i"] -> ["Ali"]. peki bu 1 milyon data içerseydi. insert veya remove komutu kullanmak zorunda
#kalsaydın ne olurdu? her bir indexi sağa ve sola kaydırmak zorunda kalıp, boşuna işlem yapacaktın.
#Hard diskleri düşün. tüm belgeler bu şekilde olsaydı bilgisayar onları yüklemek için ayrı zaman harcıyordu zaten Şimdi silmek için de zaman harcayacak.
#Çalışırken hafızasını ayarlar.

#Singly Linked list = data + sonraki datanın adresi
#ARTILARI = remove, insert komutları zaman harcamaz.
#EKSİLERİ = içinden bir dataya ulaşmak zaman alır çünkü index yok.

#Doubly Linked list = önceki datanın adresi + data + sonraki datanın adresi
#ARTILARI = hem liste başından, hem sonundan arama yapabilirsin.
#EKSİLERİ = daha fazla hafıza gerektirir.


"""
  // *******************************************************
  // LinkedList =  Nodes are in 2 parts (data + address)
  //                        Nodes are in non-consecutive memory locations
  //                        Elements are linked using pointers

  //    advantages?
  //    1. Dynamic Data Structure (allocates needed memory while running)
  //    2. Insertion and Deletion of Nodes is easy. O(1)
  //    3. No/Low memory waste

  //    disadvantages?
  //    1. Greater memory usage (additional pointer)
  //    2. No random access of elements (no index [i])
  //    3. Accessing/searching elements is more time consuming. O(n)

  //    uses?
  //    1. implement Stacks/Queues
  //    2. GPS navigation
  //    3. music playlist
  // *******************************************************
"""

from collections import deque

data = deque()
data.append("b")
data.append("c")
data.append("d")
data.append("f")
data.append("g")
data.appendleft("0")
data.insert(4,"e")
print(data)
data.rotate(-1)
print(data)
data.remove("0")
print(data)
