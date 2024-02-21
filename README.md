# Projenin İşleyişi

1. `class Kişi():`: Kişi sınıfını tanımlar.
2. `def __init__(self, isim, soyisim, numara):`: Kişi sınıfının başlatıcı yöntemidir. Yeni bir Kişi nesnesi oluşturulurken çağrılır ve isim, soyisim ve numara parametreleri alır.
3. `self.isim = isim`: Kişi nesnesinin `isim` özelliğini tanımlar ve parametre olarak gelen isim değerini atar.
4. `self.soyisim = soyisim`: Kişi nesnesinin `soyisim` özelliğini tanımlar ve parametre olarak gelen soyisim değerini atar.
5. `self.numara = numara`: Kişi nesnesinin `numara` özelliğini tanımlar ve parametre olarak gelen numara değerini atar.
6. `kişiler = []`: Kişilerin depolanacağı bir liste oluşturur.
7. `while True:`: Sonsuz bir döngü başlatır.
8. `print("Kişi Kayıt : 1\nKişileri Görüntüle : 2\nÇıkış : 0")`: Kullanıcıya seçenekleri gösteren bir menü yazdırır.
9. `işlem = int(input("İşlem Giriniz: "))`: Kullanıcıdan bir işlem seçmesini ister.
10. `if işlem == 1:`: Eğer kullanıcı 1'i seçerse, yeni bir kişi kaydı yapılmasını sağlar.
11. `isim = input("İsim giriniz: ")`: Kullanıcıdan kişinin adını alır.
12. `soyisim = input("Soyisim giriniz: ")`: Kullanıcıdan kişinin soyadını alır.
13. `numara = int(input("Numara giriniz: "))`: Kullanıcıdan kişinin numarasını alır.
14. `kişi = Kişi(isim, soyisim, numara)`: Girilen bilgilerle yeni bir Kişi nesnesi oluşturur.
15. `kişiler.append(kişi)`: Oluşturulan Kişi nesnesini kişiler listesine ekler.
16. `elif işlem == 2:`: Eğer kullanıcı 2'yi seçerse, kaydedilmiş kişilerin listelenmesini sağlar.
17. `if not kişiler:`: Eğer kişiler listesi boşsa, hiçbir kişi kaydedilmediğini belirtir.
18. `else:`: Aksi takdirde, kişileri listeler ve her bir kişinin isim, soyisim ve numarasını ekrana yazdırır.
19. `elif işlem == 0:`: Eğer kullanıcı 0'ı seçerse, programdan çıkılır.
20. `break`: Sonsuz döngüden çıkış yapar.


# Bu Projenin Bana Kattıkları
### Bilgi kaydetme,bilgi görüntüleme, hata kontrolu, kullanıcı dostu arayüz tasarımı hakkında bilgi kazandırdı.
