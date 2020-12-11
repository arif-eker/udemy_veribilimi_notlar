#           Fonksiyonlar Nasıl Yazılır?



#       def, fonksiyon tanımlamak için gereklidir.
#       parantezlerden sonra " : " konur.


def kare_al(x):
    
    print(x**2)
    
kare_al(3)


########################################################################################

#           Bilgi notuyla çıktı üreten fonksiyon

def kare_al(x):
    
    print("Girilen sayının karesi: " + str(x**2))
    
kare_al(3)



def kare_al(x):
    
    print("Girilen sayı : " + 
          str(x) + 
          ", Karesi : " +
          str(x**2))
    
kare_al(3)

########################################################################################


#           İki Argümanlı Fonksiyon Tanımlama


def carpma_yap(x,y):
    
    print(x*y)


carpma_yap(2,3)

########################################################################################

#           Ön Tanımlı Argümanlar

#       y değeri verilmezse default 1 olur. verilirse o değerle çarpar.

def carpma_yap(x,y=1):
    print(x*y)
    

carpma_yap(3)
carpma_yap(3,4)
    


#       Argümanların Sıralaması
    
carpma_yap(y = 4 , x = 5)

########################################################################################

#           Fonksiyon Çıktılarını Girdi Olarak Kullanmak



def direk_hesap(isi,nem,sarj):
    
    return ((isi+nem)/sarj)


direk_hesap(25,40,70)*9

cikti=direk_hesap(25,40,70)

print(cikti)


########################################################################################

#           Local ve Global Değişkenler

x=10

y=20

def carpma_yap(x,y):
    
    return x*y


carpma_yap(2,3)

########################################################################################


#           Local etki alanından Global etki alanını değiştirmek


x=[]

def eleman_ekle(y):
    
    #localde bir x ile alakalı değişken bulamadığından, globaldeki x nesnesini kullanır.
    
    x.append(y)
    print(str(y)+" ifadesi eklendi")

eleman_ekle("ali")

eleman_ekle("veli")

x























