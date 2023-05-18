class Magaza :

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
 
                            
def main ():
    pass
    
if __name__ == "__main__":
    main()