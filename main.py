import doktor               #gerekli kütüphaneler import edildi
import pandas as pd
import hasta
import hemsire
import personel
from datetime import datetime #hasta dogum tarihleri kontrolü icin
import sys

hasta1DogumTarihi="10.05.1990"
hasta2DogumTarihi="15.12.1992"
hasta3DogumTarihi="20.05.1970"
hastaDogumTarihleri=[hasta1DogumTarihi,hasta2DogumTarihi,hasta3DogumTarihi]
#dataframe yazilacak hasta dogum tarihleri 1990'a göre kontrol icin
dataFrameYazilacak=[]
for dogumTarihi in hastaDogumTarihleri:
    tarih=datetime.strptime(dogumTarihi,"%d.%m.%Y")
    dataFrameYazilacak.append(tarih)
#personel sınıfından  2 örnek
personel1 = personel.Personel(1, "Ahmet", "Yılmaz", "İdari", 6000)
personel2 = personel.Personel(2, "Ayşe", "Kaya", "Muhasebe", 6500)
#doktor sınıfından 3 örnek
doktor1 = doktor.Doktor(3, "Mehmet", "Demir", "Dahiliye", 9000, "Kardiyoloji", 10, "Hastane A")
doktor2 = doktor.Doktor(4, "Fatma", "Şahin", "Cerrahi", 8500, "Ortopedi", 8, "Hastane B")
doktor3= doktor.Doktor(11,"Doktor","Bey","Dahiliye",9000,"ruh ve sinir",6,"Hastane c")
#hemsire sınıfından 3 örnek
hemsire1 = hemsire.Hemsire(5, "Ali", "Çelik", "Acil", 7500, 16, "İlk Yardım", "Hastane A")
hemsire2 = hemsire.Hemsire(6, "Zeynep", "Toprak", "Pediatri", 7200, 12, "Yenidoğan Bakım", "Hastane B")
hemsire3 = hemsire.Hemsire(7, "Zeynep", "Hanım", "Pediatri", 7200, 12, "Yenidoğan Bakım", "Hastane B")
#hasta sınıından 3 örnek 
hasta1 = hasta.Hasta(666, "Ali", "Yılmaz",dataFrameYazilacak[0], "grip", "özel")
hasta2 = hasta.Hasta(333, "Ayşe", "Kaya", dataFrameYazilacak[1] , "zehirlenme", "özel")
hasta3 = hasta.Hasta(66, "Fatma", "Demir", dataFrameYazilacak[2] , "depresyon", "normal")

hasta1_ad=hasta1.get_ad()
hasta1_soyad=hasta1.get_soyad()
hasta1_ad_soyad=hasta1_ad+" "+hasta1_soyad
hasta2_ad_soyad= str(hasta2.get_ad()+" "+hasta2.get_soyad()) 
hasta3_ad_soyad= str(hasta3.get_ad()+" "+hasta3.get_soyad())

doktorun_hastalar={hasta1_ad_soyad:0,hasta2_ad_soyad:0,hasta3_ad_soyad:0} # doktor ve hemsire sınıfının hasta sınıfıyla bağlantılı olması için hastalar orada cagırılıcak sekilde sözlüge eklendi
hemsirenin_hastalar={hasta1_ad_soyad:0,hasta2_ad_soyad:0,hasta3_ad_soyad:0}

if doktor1.sorumlu_hastalar()==None: #bir doktor hep bosta kalıyor
    sys.exit()

#bilgileri yazdırma
tumKisiler=[personel1,personel2,doktor1,doktor2,doktor3,hemsire1,hemsire2,hemsire3,hasta1,hasta2,hasta3]
print("personel bilgileri")
for kisi in tumKisiler:
    print("\n",kisi,"\n")

    # hastanın personel nosu yok
nolar=[personel1.get_personel_no(),personel2.get_personel_no(),doktor1.get_personel_no(),doktor2.get_personel_no(),doktor3.get_personel_no(),
       hemsire1.get_personel_no(),hemsire2.get_personel_no(),hemsire3.get_personel_no(),hasta1.get_hastaNo(),hasta2.get_hastaNo(),hasta3.get_hastaNo()]




adlar=[personel1.get_ad(),personel2.get_ad(),doktor1.get_ad(),doktor2.get_ad(),doktor3.get_ad(),
       hemsire1.get_ad(),hemsire2.get_ad(),hemsire3.get_ad(),hasta1.get_ad(),hasta2.get_ad(),hasta3.get_ad()] #ad ve soyadlar accsesor metod ile çağırıldı


soyadlar=[personel1.get_soyad(),personel2.get_soyad(),doktor1.get_soyad(),doktor2.get_soyad(),doktor3.get_soyad(),
       hemsire1.get_soyad(),hemsire2.get_soyad(),hemsire3.get_soyad(),hasta1.get_soyad(),hasta2.get_soyad(),hasta3.get_soyad()]


departmanlar = [
    personel1.get_departman(), personel2.get_departman(),
    doktor1.get_departman(), doktor2.get_departman(), doktor3.get_departman(),
    hemsire1.get_departman(), hemsire2.get_departman(), hemsire3.get_departman(),
    None, None, None  #Hasta nesnelerinin departman özelliği olmadığı için None ekledim    
    ]

maaslar = [
    personel1.get_maas(), personel2.get_maas(),
    doktor1.maas_arttir(), doktor2.maas_arttir(), doktor3.maas_arttir(),
    hemsire1.maas_arttir(), hemsire2.maas_arttir(), hemsire3.maas_arttir(),
    None, None, None  # Hasta nesneleri için maaş özelliği olmadığı için None ekledim #maaslar arttırılmıs halleriyle dataframe yazıldı
]

#doktor uzmanliklar ve deneyim_yillari
uzmanliklar = [
    None, None,
    doktor1.get_uzmanlik(), doktor2.get_uzmanlik(), doktor3.get_uzmanlik(),
    None, None, None,
    None, None, None  # uzmanlık özelliği olmayan nesneler için None ekledim
]

deneyim_yillari = [
    None, None,
    doktor1.get_deneyim_yili(), doktor2.get_deneyim_yili(), doktor3.get_deneyim_yili(),
    None, None, None,
    None, None, None  # deneyim yılı özelliği olmayan neneler için None ekledim
]

# Hasta için hastaliklar ve tedaviler
hastaliklar = [
    None, None, None, None, None, None, None, None,
    hasta1.get_hastalik(), hasta2.get_hastalik(), hasta3.get_hastalik()
]

tedaviler = [
    None, None, None, None, None, None, None, None,
    hasta1.get_tedavi(), hasta2.get_tedavi(), hasta3.get_tedavi()
]

#hemşire için calisma_saati ve sertifikalar
calisma_saati = [
    None, None, None, None, None,
    hemsire1.get_calisma_saati(), hemsire2.get_calisma_saati(), hemsire3.get_calisma_saati(),
    None, None, None  # çalışma saati özelliği olmayan nesneler için None ekledim
]

sertifikalar = [
    None, None, None, None, None,
    hemsire1.get_sertifika(), hemsire2.get_sertifika(), hemsire3.get_sertifika(),
    None, None, None  # sertifika özelliği olmayan nesneler için None ekledim
]

dogum_tarihleri = [
    None, None, None, None, None, None, None, None,
    hasta1.get_dogumTarihi(), hasta2.get_dogumTarihi(), hasta3.get_dogumTarihi()
]
try:
    # sınıflardan alınan bilgilerin tam dogru alınıp alınamadığı kontrol ediliyor
    print("dataframe:")
    my_dict={"nolar":nolar,"ad":adlar,"soyad":soyadlar,"departman":departmanlar,"maas":maaslar,"uzmanlik":uzmanliklar,"deneyim yili":deneyim_yillari,
            "calisma saati":calisma_saati,"sertifika":sertifikalar,"dogum tarihi":dogum_tarihleri,"hastalik":hastaliklar,"tedavi":tedaviler} #dataframe data olarak verilen sözlük
    #datafrrame olusturuldu
    myDataFrame=pd.DataFrame(my_dict) # sozluk keyleri dataframe sütunları
        
    myDataFrame.fillna(0,inplace=True)  #none degerler 0 yapıldı inplace=true ile dataframe güncellendi
    print(myDataFrame)


    # doktorları uzmanlığa göre gruplayıp sayılarını bulma
    print("\nDoktorların uzmanlıklari")
    # Doktorları uzmanlık alanlarına göre gruplandırma ve yazdırma
    filterFrame=myDataFrame[myDataFrame["uzmanlik"] != 0] # uzmnligi olmayan nesneler olmadıpı bir dtaframe elde edildi
    uzmanlik_grup=filterFrame.groupby('uzmanlik').size() #uzmanlığa göre gruplandırıp her birinin sayısını .size fonksiyonu ile buldum
    print("\nUzmanlık alanlarına göre doktor sayıları:",uzmanlik_grup)


    # 5 yıldan fazla deneyime sahip doktorları bulma
    doktorlar_fazla_5_yil=myDataFrame[myDataFrame['deneyim yili'] > 5] #5 yıldan fazla deneyime sahip doktorlarda dataframe type'ında
    print("\n5 yıldan fazla deneyime sahip doktorlar:")
    print(doktorlar_fazla_5_yil)


    doktor_sayisi=doktorlar_fazla_5_yil.shape[0] #shape metodu 1. elemani satir sayisi 2. elemanı sütun sayısı oln tuple döndürür
    print("\n5 yildan fazla deneyime sahip doktor sayisi:",doktor_sayisi)

    #alfabetik olarak sıralanan hasta adlari
    #sadece hastaların dogum tarihi none degil o yüzden dogum tarihi sütununa göre grupladım
    df_hastalar=myDataFrame[myDataFrame["dogum tarihi"] !=0]
    sirali_hastalar=df_hastalar.sort_values('ad')
    print("\nHasta adına göre alfabetik sıralama")
    print(sirali_hastalar["ad"])

    #maasi 7000 den buyuk olanlar
    maas_filtre=myDataFrame[myDataFrame["maas"]>=7000]
    print("\nMaaşı 7000 tlden fazla personeller\n",maas_filtre)

    #dogum tarihine göre hastalar

    #sadece hastaların dogum tarihi değerleri 0 olmdığı  için bir ayırma yapmadan direkt dataframe olusturdum
    myDataFrame['dogum tarihi']=pd.to_datetime(myDataFrame['dogum tarihi']) #pd.to_datetime() fonksiyonu, verilen tarih verilerini pandas'ın anlayabileceği bir datetime formatına dönüştürüyor

    # Doğum tarihi 1990 ve sonrası olan hastaları filtreledim
    filtre=myDataFrame['dogum tarihi'].dt.year >= 1990
    hastalarFiltrelenmis=myDataFrame[filtre]

    print("\nDoğum tarihi 1990 ve sonrası olan hastalar:")
    print(hastalarFiltrelenmis)

    #Var olan DataFrame’den ad, soyad, departman, maas, uzmanlik, deneyim_yili,hastalik, tedavi bilgilerini içeren yeni bir DataFrame oluşturup yazma #tedavi süresi sadece hastalar icin var
    yeniDf=myDataFrame[['ad','soyad','departman','maas','uzmanlik','deneyim yili','hastalik','tedavi']] #belirli sütunlari iceriyor
    #Yeni DataFrame'i yazdırma
    print("Yeni DataFrame:")
    print(yeniDf)
    
except:
    print("Nesneler oluşturulamadı")