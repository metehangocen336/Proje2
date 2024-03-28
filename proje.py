def kitap_ekle():
    with open("kitaplar.txt", "a") as dosya:
        kitap_adı = input("Eklemek istediğiniz kitabın adını girin: ")
        yazar_adı = input("Yazarın adını girin: ")
        isbn_no = input("ISBN numarasını girin: ")
        dosya.write(f"{kitap_adı},{yazar_adı},{isbn_no}\n")
        print(f"{kitap_adı} başarıyla eklendi.")

def mevcut_kitaplar():
    print("Mevcut kitaplar:")
    with open("kitaplar.txt", "r") as dosya:
        for satır in dosya:
            kitap_adı, _, _ = satır.strip().split(",")
            print(kitap_adı)

def odunc_al():
    odunc_alinanlar = {}
    mevcut_kitaplar()
    secilen_kitap = input("Hangi kitabı ödünç almak istersiniz? (Kitap adını girin): ")
    secim = input("Hangi bilgiyi görmek istersiniz? (1-Yazar, 2-ISBN): ")
    kullanici_adi = input("Ödünç alan kişinin adını girin: ")
    with open("kitaplar.txt", "r") as dosya:
        for satır in dosya:
            kitap_adı, yazar_adı, isbn_no = satır.strip().split(",")
            if kitap_adı == secilen_kitap:
                if secim == "1":
                    bilgi = yazar_adı
                elif secim == "2":
                    bilgi = isbn_no
                odunc_alinanlar[kullanici_adi] = {"kitap": kitap_adı, "bilgi": bilgi}
                print(f"{kitap_adı} {kullanici_adi} adlı kişiye ödünç alındı. ({'Yazar' if secim == '1' else 'ISBN'}: {bilgi})")
                break
        else:
            print("Böyle bir kitap mevcut değil.")
    
    return odunc_alinanlar

kitap_ekle()
odunc_alinan_kitaplar = odunc_al()
print("Ödünç Alınan Kitaplar:")
for kullanici, bilgiler in odunc_alinan_kitaplar.items():
    kitap = bilgiler["kitap"]
    bilgi = bilgiler["bilgi"]
    print(f"{kullanici}: {kitap} - {'Yazar' if isinstance(bilgi, str) else 'ISBN'}: {bilgi}")