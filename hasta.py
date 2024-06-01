class Hasta():
    def __init__(self,hastaNo,ad,soyad,dogumTarihi,hastalik,tedavi):
        self.__hastaNo=hastaNo
        self.__ad=ad
        self.__soyad=soyad
        self.__dogumTarihi=dogumTarihi
        self.__hastalik=hastalik
        self.__tedavi=tedavi
        

    def get_hastaNo(self):  #get ve set metodlari
        return self.__hastaNo

    def set_hastaNo(self, hastaNo):
        self.__hastaNo = hastaNo

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_dogumTarihi(self):
        return self.__dogumTarihi

    def set_dogumTarihi(self, dogumTarihi):
        self.__dogumTarihi = dogumTarihi

    def get_hastalik(self):
        return self.__hastalik

    def set_hastalik(self, hastalik):
        self.__hastalik = hastalik

    def get_tedavi(self):
        return self.__tedavi

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi
    def tedavi_suresi_hesapla(self):
        hastaliklar={"grip":3,"zehirlenme":7,"depresyon":30}
        mevcut_hastalik=self.get_hastalik()
        mevcut_hastalik_tedavi_süre=""
        uygulanacak_tedavi_süre=""
        tedaviler={"özel":2,"normal":4}
        mevcut_tedavi=self.get_tedavi()
        for x in hastaliklar.keys():
            if mevcut_hastalik==x:
                mevcut_hastalik_tedavi_süre=hastaliklar[x]
        for y in tedaviler.keys():
            if mevcut_tedavi==y:
                uygulanacak_tedavi_süre=tedaviler[y]
        tedavi_süresi= mevcut_hastalik_tedavi_süre + uygulanacak_tedavi_süre
        return tedavi_süresi
    def __str__(self):
        return f"hasta no:{self.__hastaNo} ad {self.__ad}, soyad {self.__soyad}, dogum tarihi {self.__dogumTarihi}, hastalik {self.__hastalik}, tedavi {self.__tedavi}"