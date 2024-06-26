import personel # kalıtım için
class Doktor(personel.Personel): 
    def __init__(self, personel_no, ad, soyad, departman, maas,uzmanlik,deneyim_yili,hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane 
        #get metodlari
    def get_uzmanlik(self):
        return self.__uzmanlik
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    def get_hastane(self):
        return self.__hastane
        #set metodlari
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik
    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili
    def set_hastane(self,hastane):
        self.__hastane=hastane
    def maas_arttir(self):
        maas=self.get_maas()
        arttirilmis_maas= maas + (self.__deneyim_yili*1000) # maas deneyim yılınin 1000 çarpılmasi kadar artiyor
        return arttirilmis_maas
    
    def sorumlu_hastalar(self):
        from main import doktorun_hastalar
        for hasta,dolumu in doktorun_hastalar.items():
            if doktorun_hastalar[hasta]==0:  #hastanin valuesu 0 olarak atandi burada 1 arttırılıyor eger 1 artarsa hastaya doktor denk geliyor ve birdaha yeni bir doktorla eslesmiyor
                doktorun_hastalar[hasta]+=1
                return hasta
    def __str__(self):
        # önce diğer sınıflardan gelen bilgiler sonra doktor sınıfından gelen bilgiler
        return f"{super().__str__()}, uzmanlık: {self.__uzmanlik}, deneyim yılı: {self.__deneyim_yili}, hastane: {self.__hastane}, arttirilmis maas={self.maas_arttir()},sorumlu oldugu hasta:{self.sorumlu_hastalar()}"