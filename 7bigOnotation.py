"""
Data büyüdükçe kodun çalışma süresinin değişimini gösteren fonksiyon.

-performans analizi için kullanılır.
-makineden bağımsız olarak algoritmaların verimliliğini analiz etmek için kullanılır. kaç işlem yapıldığını gösterir.
-düşük değerler daha iyi performans anlamına gelir.
-küçük işlemler önemli değildir, büyük işlemler önemlidir. n + 1  yerine n deriz. n büyüdükçe 1 önemsiz hale gelir.
örnekler:
O(1) - Sabit zaman: İşlem sayısı veri büyüklüğüne bağlı değildir.
O(n) - Doğrusal zaman: İşlem sayısı veri büyüklüğü ile doğru orantılıdır.
O(n^2) - Kare zaman: İşlem sayısı veri büyüklüğünün karesi ile orantılıdır.
o(log n) - Logaritmik zaman: İşlem sayısı veri büyüklüğünün logaritması ile orantılıdır.
"""
import time

def addUp(num=0):
    total = 0
    time_start = time.time()
    for i in range(num+1):
        total += i
    time_end = time.time()
    executed_time = time_end - time_start
    return total, executed_time

def sum2_2(num=0):
    total = 0
    time_start = time.time()
    total = (num * (num + 1)) // 2
    time_end = time.time()
    executed_time = time_end - time_start
    return total, executed_time

num = 1000
print(f"\nSteps that will be executed are equal to num: O({num}) \n")
print(f"Test addUp: \nTotal={addUp(num)[0]} \nExecuted Time={addUp(num)[1]} seconds\n"+"-"*50)

print(f"\nSteps that will be executed are equal to num: O(~1) \n")
print(f"Test sum2_2: \nTotal={sum2_2(num)[0]} \nExecuted Time={sum2_2(num)[1]} seconds")
