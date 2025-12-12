"""
LIFO: Last In First Out - Son Giren İlk Çıkar 


// recursion = Bir şeyin kendisiyle tanımlanması. - Wikipedia
//      Bir prosedürün sonucunu, bir prosedüre uygular.
//      Özyinelemeli(recursive) bir yöntem kendini çağırır. İterasyonun yerine geçebilir.
//      Bir problemi, orijinaliyle aynı türden alt problemlerine böler.
//      Genellikle gelişmiş sıralama algoritmaları ve ağaçlarda gezinme ile kullanılır.

# bakınız:
# references\\recursive.png, references\\recursive_2.png, references\\recursive_3.png

Avantajları:
- Bazı problemler için daha basit ve daha temiz çözümler sunar.
- Debugging ve kod okuma daha kolay olabilir.

Dezavantajları:
- Bellek kullanımı daha yüksektir (çağrı yığını nedeniyle).
- Performans açısından iteratif çözümlerden daha yavaş olabilir.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))  # Beklenen çıktı: 120