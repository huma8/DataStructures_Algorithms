"""
SÖZLÜKLER bu mantıkla çalışır:

// Hashtable = A data structure that stores unique keys to values    
                          Each key/value pair is known as an Entry
                          FAST insertion, look up, deletion of key/value pairs
                          Not ideal for small data sets, great with large data sets

// hashing = Takes a key and computes an integer (formula will vary based on key & data type)
//		       In a Hashtable, we use the hash % capacity to calculate an index number 
//			key.hashCode() % capacity = index 

O(1) average time complexity for insert, delete, search

| Kavram              | Basit Anlatım                             |
| ------------------- | ----------------------------------------- |
| Hash Table          | Anahtar-değer saklayan özel yapı          |
| Hash Fonksiyonu     | Anahtarı tablo konumuna çeviren fonksiyon |
| Ekleme ve Arama     | Anahtar → hash → indeks → değer           |
| Çakışma (Collision) | Aynı hash sonucu → çözüm gerekir          |
| Performans          | Hızlı (ortalama O(1))                     |
| bucket              | Birden çok girişi saklayan konum          |
| ------------------- | ----------------------------------------- |
                          
bakınız:
references\hash-table.png, references\hash-table2.png
"""

hashtable = {"name": "Alice", "age": 30, "city": "New York"}

print(hashtable["name"])  # Output: Alice
print(hashtable["age"])   # Output: 30
print(hashtable["city"])  # Output: New York


