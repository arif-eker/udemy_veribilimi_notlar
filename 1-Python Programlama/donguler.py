

#           For Döngüsü

ogrenci=["ali","veli","ışık","berk"]

for i in ogrenci:
    print(i)

###########################################
    
#       Örnek 1
    
    
def kare_al(x):
    print(x**2)


kare_al(2)

maaslar=[1000,2000,3000,4000]

for item in maaslar:
    print(item)



#   Maaşlara %20 zam yapılacak olsun.


def yeni_maas(x):
    print(x*0.2+x)


for items in maaslar:
    yeni_maas(items)



##############################################
    
#       Örnek 2
    
maaslar=[1000,2000,3000,4000,5000]

def maas_ust(x):
    print(x*0.1+x)

def maas_alt(x):
    print(x*0.2+x)
    
for items in maaslar:
    
    if items >= 3000:
        maas_ust(items)

    else: 
        maas_alt(items)

####################################################

#       break & continue ifadeleri
        
maaslar=[8000,5000,2000,1000,3000,7000,1000]

#küçükten büyüğe sırala
maaslar.sort()

for items in maaslar:
    
    if items==3000:
        
        print("kesildi")
        
        break

    print(items)

for items in maaslar:
    
    if items==3000:  
        continue

    print(items)

########################################################
    
#           While Döngüsü
    

sayi=1

#sayi 10'dan küçük olduğu sürece çalıştır.

while sayi < 10:
    sayi += 1
    
    print(sayi)













