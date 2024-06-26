import personel
class Hemsire(personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati,sertifika,hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati=calisma_saati
        self.__sertifika=sertifika
        self.__hastane=hastane
    # get metodlari
    def get_calisma_saati(self):
        return self.__calisma_saati
    def get_sertifika(self):
        return self.__sertifika
    def get_hastane(self):
        return self.__hastane
    # set metodları
    def set_calisma_saati(self,calisma_saati):
        self.__calisma_saati=calisma_saati
    def set_sertifika(self,sertifika):
        self.__sertifika=sertifika
    def set_hastane(self,hastane):
        self.__hastane=hastane
    def maas_arttir(self):
        maas= self.get_maas()
        arttirilmis_maas= maas +(self.__calisma_saati *20) # maas artisi calısma saatinin 20 katı kadar
        return arttirilmis_maas
    def sorumlu_hastalar(self):
        from main import hemsirenin_hastalar # hastalar döngüsel hata olmaması icin yerel olark olusturuldu
        for hasta in hemsirenin_hastalar.keys():
            if hemsirenin_hastalar[hasta]==0:  #hastanin valuesu 0 olarak atandi burada 1 arttırılıyor eger 1 artarsa hastaya hemsire denk geliyor ve birdaha yeni bir hemsire ile eslesmiyor
                hemsirenin_hastalar[hasta]+=1
                return hasta
    def __str__(self):
        return f"{super().__str__()}, calisma saati={self.__calisma_saati},sertifika={self.__sertifika},hastane={self.__hastane}, arttirilmis maas={self.maas_arttir()}, sorumlu oldugu hasta:{self.sorumlu_hastalar()}"