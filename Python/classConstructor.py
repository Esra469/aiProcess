
"""

"""
#Class

class Calisan:
    zam_orani=1.8
    
    counter=0
    
    def __init__(self,isim,soyisim,maas): #constractor
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"asd.com"
        Calisan.counter=Calisan.counter+1#classı artırıyoruz metodu değil
        
        
    def giveMeSurname(self):
         return self.isim+" "+self.soyisim
    def zam_yap(self):
        self.maas=self.maas+self.maas*self.zam_orani
        
isci1=Calisan("Esra","cimen", 100)
print(isci1.giveMeSurname)

"""
isci.isim->ismi verir direkt
isci.soyisim->soyismi verir direkt
"""
#class variable
calisan1=Calisan("Ali", "veli",200)
print("ilk maas",calisan1.maas)
calisan1.zam_yap()
print("yeni maaş ",calisan1.maas)


