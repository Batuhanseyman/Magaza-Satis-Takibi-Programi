class Magaza :

    magaza_toplamlari = []
    magaza_dict = {}
    
    def __init__ (self, magaza_adi, satici_adi, satici_cinsi):

        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi

    def set_magaza_adi (self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def set_satici_adi (self, satici_adi):
        self.__satici_adi = satici_adi

    def set_satici_cinsi (self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi
    
    def get_magaza_adi (self):
        return self.__magaza_adi
    
    def get_satici_adi (self):
        return self.__satici_adi
    
    def get_satici_cinsi (self):
        return self.__satici_cinsi
    
    def magaza_satis_tutar (self, satis_verileri):
        #Parametre olarak gelen dictionary'nin yapısı hakkında örnek:
        #{flo: {('Ali', 'diğer'):[780, 850], ('Veli', 'diğer'):[1200, 685]}, vestel:{('ece', 'beyaz eşya'):[12000, 5500],('ada', tv):[5450, 10500]}}
        for key1 in satis_verileri:
            for key2, val in satis_verileri[key1].items():
                satici_top = sum(val)
                satis_verileri[key1][key2] = [satici_top]
                Magaza.magaza_dict = satis_verileri
                #Dictionary'nin yeni hali ve magaza_dict'in içeriğine dair örnek
                #{flo: {('Ali', 'diğer'):[1630], ('Veli', 'diğer'):[1885]}, vestel:{('ece', 'beyaz eşya'):[17500],('ada', tv):[15950}}
        
        for qey1 in satis_verileri:
            toplam = []
            for value in satis_verileri[qey1].values():
                toplam += value
                if qey1 not in Magaza.magaza_toplamlari:
                    Magaza.magaza_toplamlari.append(qey1)
                    Magaza.magaza_toplamlari.append(sum(toplam))
                else:
                    store = Magaza.magaza_toplamlari.index(qey1)
                    Magaza.magaza_toplamlari[store + 1] = sum(toplam)
                    #magaza_toplamlari listesinin örnek verilen dictionary'e göre örneği
                    #['flo', 3515, 'vestel', 33450]     


    def __str__(self):
        toplamlar = ""
        for i in range (0, len(Magaza.magaza_toplamlari), 2):
            toplamlar += f"{Magaza.magaza_toplamlari[i]} adli magazanin toplam satis tutari = {Magaza.magaza_toplamlari[i+1]}₺\n"

        toplamlar += "\n"
        
        for key1 in Magaza.magaza_dict:
            for key2, val in Magaza.magaza_dict[key1].items():
                toplamlar += f"{key1} adli magazada calisan ve {key2[1]} saticisi olan {key2[0]} adli saticinin toplam satis tutari = {val[0]}₺\n"
        return toplamlar 
                            
def main ():
    satislar = {}
    print ("----------Satis bilgilerini giriniz-----------")
    print ("")

    while True:

        magaza_adi = input ("Mağazanin adini giriniz : ")
        satici_adi = input ("Saticinin adini giriniz : ")
        satici_cinsi = input ("Saticinin cinsini giriniz" +
         " (tv, bilgisayar, beyaz eşya, diğer) : ")
        satis_tutari = float (input("Saticinin satis tutarini giriniz : "))
        print("")
        satis = Magaza(magaza_adi.strip().capitalize(), satici_adi.strip().capitalize(), satici_cinsi.strip().capitalize())
        
        key1 = satis.get_magaza_adi()
        key2 = (satis.get_satici_adi(),satis.get_satici_cinsi())

        #Tanımlanan dictionary'nin yapısı hakkında bir örnek:
        #{flo: {('Ali', 'diğer'):[780, 850], ('Veli', 'diğer'):[1200, 685]}, vestel:{('ece', 'beyaz eşya'):[12000, 5500],('ada', tv):[5450, 10500]}}
        
        if key1 not in satislar:
            satislar[key1] = {}
    
        if key2 not in satislar[key1]:
            satislar[key1][key2] = [satis_tutari]

        elif key1 in satislar and key2 in satislar[key1]:
            satislar[key1][key2].append(satis_tutari)

        satis.magaza_satis_tutar(satislar)
        print(satis)
        devam_durumu = input("Devam etmek istiyor musunuz?(e/E/h/H)")
        print("")
        if devam_durumu == "h" or devam_durumu == "H":
            break
    
if __name__ == "__main__":
    main()