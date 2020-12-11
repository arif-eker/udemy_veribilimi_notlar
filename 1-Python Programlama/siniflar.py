#           SINIFLAR




# Sınıf tanımlama

#class VeriBilimci():
#   print("Bu bir sınıftır.")
    
    
#       Sınıf Özellikleri (Attributes)
    
class VeriBilimci():
    bolum=''
    sql="Evet"
    deneyim_yili=0
    bildigi_diller=[]


#       Sınıfların özelliklerine erişmek
VeriBilimci.bolum
VeriBilimci.sql

#       Özellikleri değiştirmek

VeriBilimci.sql ="Hayır"

VeriBilimci.sql

#           Sınıf Örneklendirmesi (instantiation)

#Bu şekilde bir örneklem yaparsak eğer, arifin bildiği dili, veli de bilecektir. Bu hatalı olacaktır.
#Bunu engellemek için örnek özellikleri konusuna bakmalıyız.


arif = VeriBilimci()
arif.sql
arif.deneyim_yili

arif.bildigi_diller.append("Python")
arif.bildigi_diller



veli=VeriBilimci()
veli.sql
veli.bildigi_diller



#       Örnek Özellikleri

class VeriBilimci():
    
    
    
    #peki sınıfın kendi özelliklerini tanımlayalım.
    bolum=''
    sql=''
    deneyim_yili=0
    bildigi_diller=["R","Python"]
    
    #Bu şekilde bir tanımlama, her örnek için kendi içinde değişen özellik tanımlamayı sağlar.
    #ali veya veli için de farklı değerler alabilir. ali.bildigi_diller demek veliyi etkilemeyecek.
    #örneklerin kendi özellikleri
    def __init__(self):
        self.bildigi_diller=[]
        self.bolum=''


ali= VeriBilimci()
veli=VeriBilimci()

ali.bildigi_diller
veli.bildigi_diller


ali.bildigi_diller.append("Python")

ali.bildigi_diller

veli.bildigi_diller

veli.bildigi_diller.append("R")
veli.bildigi_diller

VeriBilimci.bildigi_diller

VeriBilimci.bildigi_diller.append("Kalk")
VeriBilimci.bildigi_diller


# ! self örneklemleri temsil eder. yani temsilcidir. yerine farklı bir şey de yazılabilir ama self yazmak önemli.

# sınıf özellikleri ile self özelliklerinin isimlendirmeleri farklı olması iyi olacaktır.




#           Örnek Metodları




class VeriBilimci():
        
    calisanlar=[]
    
    def __init__(self):
        
        self.bildigi_diller=[]
        self.bolum=''
                        
    def dil_ekle(self,yeni_dil):
        
        self.bildigi_diller.append(yeni_dil)




ali=VeriBilimci()

ali.bildigi_diller
ali.bolum

veli=VeriBilimci()

veli.bildigi_diller
veli.bolum

ali.dil_ekle("R")

veli.dil_ekle("Python")

ali.bildigi_diller

veli.bildigi_diller



#           Miras Yapıları (inheritance)

class Employees():
    
    def __init__(self):
        
        self.FirstName=''
        self.LastName=''
        self.Address=''


class DataScience(Employees):
    
    def __init__(self):
        
        self.Programming=''
       


veribilimci1 = DataScience()
veribilimci1.Address


class Marketing(Employees):
    
    def __init__(self):
        
        self.StoryTelling=''

mar=Marketing()
mar.Address


class Employees_yeni():
    
    def __init__(self,FirstName,LastName,Address):
        
        self.FirstName=FirstName
        self.LastName=LastName
        self.Address=Address


deneme=Employees_yeni("a", "b","c")

deneme.Address

















