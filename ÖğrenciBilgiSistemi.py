def ogrenci_ekle():
    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt","a",encoding = "utf-8") as f:
        ogrenci = {}
        isim = input("Ogrenci ismini giriniz: ")
        ogrenci["soyad"] = isim
        soyisim = input("Ogrenci soyismini giriniz: ")
        ogrenci["ad"] = soyisim
        notlar = input("Ogrenci notunu giriniz: ")
        ogrenci["notlar"] = notlar
        f.write(f"{isim},{soyisim},{notlar}\n")
        print("Ogrenci başariyla kaydedildi!!!")

def ogrenci_sil():
    isim = input("Silinecek ogrencinin ismini giriniz: ")
    soyisim = input("Silinecek öğrencinin soyadini giriniz: ")
    
    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt","r",encoding = "utf-8") as f:
        satirlar = f.readlines()

    silindi = False

    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt","w",encoding = "utf-8") as dosya:  
            for satir in satirlar:
                bilgiler = satir.strip().split(",")
                if not (bilgiler[0] == isim and bilgiler[1] == soyisim):
                    dosya.write(satir)
                else:
                    silindi = True

            if silindi:
                print("Öğrenci silindi.")
            else:
                print("Öğrenci bulunamadi.")    

def ogrenci_guncelle():
    isim = input("Güncellenecek öğrencinin adını giriniz: ")
    soyisim = input("Güncellenecek öğrencinin soyadını giriniz: ")
    print("Güncellemek istediğiniz veriyi seçiniz:")
    secim = input("1- İsim\n2- Soyisim\n3- Notlar\nSeçim: ")

    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt", "r", encoding="utf-8") as f:
        satirlar = f.readlines()

    yeni_satirlar = []
    guncellendi = False

    for satir in satirlar:
        bilgiler = satir.strip().split(",")  

        if len(bilgiler) >= 3 and bilgiler[0] == isim and bilgiler[1] == soyisim:

            if secim == "1":
                bilgiler[0] = input("Yeni ismi giriniz: ")
            elif secim == "2":
                bilgiler[1] = input("Yeni soyismi giriniz: ")
            elif secim == "3":
                bilgiler[2] = input("Yeni notları giriniz: ")
            else:
                print("Geçersiz seçim!")
                return

            yeni_satir = ",".join(bilgiler) + "\n"
            yeni_satirlar.append(yeni_satir)
            guncellendi = True
        else:
            yeni_satirlar.append(satir)

    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt", "w", encoding="utf-8") as f:
        f.writelines(yeni_satirlar)

    if guncellendi:
        print("Öğrenci bilgileri güncellendi!")
    else:
        print("Öğrenci bulunamadı!")

        
def ogrenci_listele():
    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt", "r", encoding="utf-8") as f:
        print(f.read())


def Sinif_ortalama():
    toplam = 0
    adet = 0

    with open("C:\\Users\\EMİRHAN\\OneDrive\\Desktop\\PYTHON\\projeler\\OgrenciBilgileri.txt", "r", encoding="utf-8") as f:
        satirlar = f.readlines()

        for satir in satirlar:
            if satir.strip() == "":
                continue  # boş satır varsa atla
            bilgiler = satir.strip().split(",")  # ['Emirhan', 'Kara', '85']
            
            try:
                toplam += float(bilgiler[2])  # notu topla
                adet += 1
            except:
                print(f"Hatalı satır atlandı: {satir}")

    if adet > 0:
        ortalama = toplam / adet
        print(f"Sınıf not ortalaması: {ortalama:.2f}")
    else:
        print("Hiç öğrenci verisi bulunamadı.")



while True:
    print("1-Ogrenci_ekle\n2-Ogrenci_sil\n3-Ogrenci_guncelle\n4-Sinif_ortalamasi\n5-Ogrenci_listele\n6-Cikis\n")
    secim = input("Secim yapiniz: ")

    if secim == "1":
        ogrenci_ekle()
    
    elif secim == "2":
        ogrenci_sil()

    elif secim == "3":
        ogrenci_guncelle()

    elif secim == "4":
        Sinif_ortalama()

    elif secim == "5":
        ogrenci_listele()
    
    elif secim == "6":
        print("Çıkılıyor...")
        break
    else:
        print("gecersiz ifade!!!")
       
