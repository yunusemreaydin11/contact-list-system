import json

class Kişi():
    def __init__(self, isim, soyisim, numara):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara

kişiler = []

while True:
    print("Kişi Kayıt : 1\nKişileri Görüntüle : 2\nÇıkış : 0")
    işlem = int(input("İşlem Giriniz: "))
    
    if işlem == 1:
        isim = input("İsim giriniz: ")
        soyisim = input("Soyisim giriniz: ")
        numara = int(input("Numara giriniz: "))

        if len(str(numara)) > 7 :
          print("Lütfen Geçerli Bir Numara Giriniz!")  

        kişi = Kişi(isim, soyisim, numara)
        kişiler.append(kişi)

        print("Kişi bilgileri kaydedildi.")
        
    elif işlem == 2:
        if not kişiler:
            print("Henüz hiçbir kişi kaydedilmedi.")
        else:
            print("Kişiler:")
            for kişi in kişiler:
                print(f"İsim: {kişi.isim}")
                print(f"Soyisim: {kişi.soyisim}")
                print(f"Numara: {kişi.numara}")
                print("-" * 20)
            
    elif işlem == 0: 
        print("Çıkış Yapılıyor...")
        break
