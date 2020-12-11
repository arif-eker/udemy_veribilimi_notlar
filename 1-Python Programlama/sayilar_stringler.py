#Say�lar

#int say�
9

#float say�
9.2

#��lemler
9*9
9/9
9+9
9-5


#Karakter Dizileri (Stringler)

"Merhaba D�nya"

'Merhaba D�nya'

###########################################################
#                                                         #
#           Bir nesnenin tipini nas�l ��reniriz?          #
#                                                         #  
#                ##########################################
#                #
    type(9)      #
    type(9.2)    #
    type("Arif") #
#                #
##################

                                   ##################################
                                   #                                #
                                   #------> String Metotlar <-------#
                                   #                                #
                                   ##################################

###########################################################
#           len() fonksiyonu                              #
#                                                         #
#       string ifadenin uzunlu�unu verir                  #
#                                                         #
#                                 #########################
#                                 #
    gel_yaz="gelecegi_yazanlar"   #
    len(gel_yaz)                  #
#                                 #
###################################



##########################################################
#           upper() & lower() fonksiyonlar�              #
#                                                        #
#                                                        #
#     string ifadeleri b�y�k/k���k harf �ekline �evirir. #
#                                                        #
#                          ###############################
#                          #
    B=gel_yaz.upper()      #
    K=gel_yaz.lower()      #
#                          #
    print(B)               #
    print(K)               #
#                          #
############################


#########################################################
#           islower() & isupper() fonksiyonu            #
#                                                       #
#      true/false d�ner                                 #
#                                                       #
#                         ###############################
#                         #
    gel_yaz.islower()     #
#                         #
    gel_yaz.isupper()     #
#                         #
###########################



#####################################################################################################
#                                       replace() metodu                                            #
#                                                                                                   #
#                                                                                                   #
#   string i�indeki harfleri de�i�tirmek i�in kullan�l�r                                            #
#                                                                                                   #
#   parantez i�indeki ilk ifade de�i�tirilmek istenen harf, ikinci ifade ise d�n��t�r�lecek harftir #
#                                                                                                   #
#                                       #############################################################
#                                       #
    print(gel_yaz.replace("e","a"))     #
    print(gel_yaz.replace("a","i"))     #
#                                       #
#########################################



##################################################################################################
#                                   strip() fonksiyonu                                           #
#                                                                                                #
#                                                                                                #
#    istenmeyen karakterleri k�rpmak i�in kullan�l�r. �n tan�m olarak bo�luklar� siler           #
#                                                                                                #
#                                          #######################################################
#                                          #
#                                          #
    gel_yaz = " gelecegi_yazanlar "        #
    len(gel_yaz)
    print(gel_yaz.strip())                 #
#                                          #
    gel_yaz = "*gelecegi_yazanlar*"        #
    print(gel_yaz.strip("*"))              #
#                                          #
############################################
    
    
    
                                    #######################################
                                    #                                     #
                                    #------> Metotlara Genel Bak�� <------#
                                    #                                     #
                                    #######################################


############################################################
#                   dir() fonksiyonu                       #
#                                                          #
#                                                          #
#  i�indeki nesneye uygulanabilecek fonksiyonlar� g�sterir #
#                                                          #
#                    #######################################
#                    #
    dir(str)         #
    dir(int)         #
    dir(gel_yaz)     #
#                    #
######################

                                   ##############################
                                   #                            #
                                   #------> SUBSTR�NGLER <------#
                                   #                            #
                                   ##############################

####################################################################
#                                                                  #
#elimizdeki stringlerin alt stringlerine ula�mak i�in kullan�r�z.  #
#                                                                  #
#                                                                  #
#                                                                  #############
    gel_yaz="gelecegi_yazanlar"                                                #
#                                                                              #
#   0. indeks                                                                  #
    gel_yaz[0]                                                                 #
#                                                                              #
#   0 dan 2 dahil almak i�in. 0:3 yazmak gerekir. 0 dahil ama 3 dahil de�ildir.#
    gel_yaz[0:3]                                                               #
#                                                                              #    
################################################################################



                                   #############################
                                   #                           #
                                   #------> DE���KENLER <------#
                                   #                           #
                                   #############################




#Say�sal De�i�kenler
type(10)
type(10.2)
type(2+1j)

#String de�i�ken
arif="Arif"
Arif='Arif'



                                   #################################
                                   #                               #
                                   #------> Tip D�n���mleri <------#
####################################                               #
#                                                                  #
#                                                                  #
#       kullan�c�dan al�nan de�erleer default olarak "stringtir"   #
#                                                                  #
        toplama_bir= input()                                       #
        toplama_iki= input()                                       #
#                                                                  #
        type(toplama_bir)                                          #
#                                                                  #
        toplama_bir + toplama_iki                                  #
                                                                   #
#tip d�n��t�rmek i�in ba��na (int) ifadeleri eklenir.              #
                                                                   #
        int(toplama_bir)+int(toplama_iki)                          #
#                                                                  #
        int(12.5)                                                  #
        float(14)                                                  #
        complex(4)                                                 #
        str(14)                                                    #
#                                                                  #
####################################################################


#######################################################################
#                                                                     #
#                       print() fonksiyonu                            #
#                                                                     #
#                                                                     #
#                                                                     #
#                                                                     #
            print("Hello ARI ERA")                                    #
            print("gelece�i","yazanlar")                              #
#                                                                     #
#           _ ile birle�tirmek i�in                                   #
#                                                                     #
            print("gelecegi","yazanlar",sep="_")                      #
#                                                                     ###############################
#                                                                                                   #
#                                                                                                   #
#                                                                                                   #
#           sep bir arg�mand�r.                                                                     #
#           fonksiyonlar�n arg�manlar�n�n nas�l kullan�laca��n� bilmek i�in ba�lar�na               #
#           soru i�areti getirmek gerekir : ?print ifadesi yaz�p �al��t�r�nca bilgi verecektir.     #
#                                                                                                   #
#####################################################################################################

#****************************************************************************************************************************#
            
#****************************************************************************************************************************#
            
#****************************************************************************************************************************#
                 
                                    ###########################################
                                    #                                         #
                                    #       ------> VER� YAPILARI <------     #
                                    #                                         #
                                    ###########################################

#################################################################################################
#                                                                                               #
#                                   ------> Listeler <------                                    #
#                                                                                               #
#                                                                                               #
#       S�ral�d�r.                                                                              #
#       De�i�tirilebilirdir.                                                                    #
#       Kapsay�c�d�r (Farkl� tipte verileri tutabilir)                                          #
#                                                                                               #
#       [] veya list() �eklinde olu�turulabilir.                                                #
#                                                                                               #
#           liste olu�turma                                                                     #
#                                                                                               #
    notlar=[90,80,70,50]                                                                        #
    type(notlar)                                                                                #
#                                                                                               #
    liste=["A",19.3,90]                                                                         #
    list_genis=["A",19.3,90,notlar]                                                             #
#                                                                                               #
    len(list_genis)                                                                             #
#                                                                                               #
#                                                                                               #
#           liste i�i tip sorgulama                                                             #
#                                                                                               #
    type(list_genis[0])                                                                         #
#                                                                                               #
#           iki listeyi birle�tirme                                                             #
    tum_liste=[liste,list_genis]                                                                #
#                                                                                               #
#           listeyi silme                                                                       #
#                                                                                               #
    del tum_liste                                                                               #
#                                                                                               #
#daha sonra bunu yorum sat�r�na al                                                              #
#                                                                                               #
#                                                                                               #
#           liste elemanlar�na eri�mek                                                          #
#                                                                                               #
    yeni_liste=[10,20,30,40,50]                                                                 #
#                                                                                               #
    yeni_liste[0:2]                                                                             #
    yeni_liste[:2]                                                                              #
    yeni_liste[2:]                                                                              #
#                                                                                               #
    baska_liste=["a",10,[20,30,40,50]]                                                          #
#                                                                                               #
#           liste i�indeki liste eleman�na eri�mek i�in:                                        #
#                                                                                               #
    baska_liste[2][1]                                                                           #
#                                                                                               #
#yani listenin 2. elaman�n�n 1. elaman�na eri�.                                                 #
#                                                                                               #      
#################################################################################################
#                                                                                               #
#           listelere eleman ekleme/de�i�tirme/silme                                            #  
#                                                                                               #      
#       Eleman De�i�tirme                                                                       #
#                                                                                               #
    liste=["ali","veli","berkcan","ayse"]                                                       #
#                                                                                               #
    liste[0:3]="alinin_babasi","velinin_babasi","berkcanin_babasi"                              #
#                                                                                               #    
#################################################################################################    
#       Eleman Ekleme                                                                           #
#   Bu �ekilde atama yapmadan ekleme yap�ld���nda, kemal listeye kal�c� olarak eklenmez.        #
#   bunun i�in atama yapmak gerekir.                                                            #
#                                                                                               #   
    liste +["kemal"]                                                                            #
    liste=liste+["kemal"]                                                                       #
#                                                                                               #    
#################################################################################################    
#       Eleman Silme                                                                            #  
#                                                                                               #
#  indeksteki eleman� silmek                                                                    #
    del liste[2]                                                                                #
#                                                                                               #    
#################################################################################################
#                                   ------> Liste Metotlar� <------                             #
#                                                                                               #
#                                                                                               #
    dir(liste)                                                                                  #
#                                                                                               #
#           append() metodu                                                                     #
#                                                                                               #
    liste.append("berkcan")                                                                     #
#                                                                                               #
#           remove() metodu                                                                     #
#                                                                                               #
    liste.remove("berkcan")                                                                     #    
#                                                                                               #
#           insert() metodu                                                                     #
#                                                                                               #
#   listenin 0. indisine "ayse" ekle                                                            #
    liste.insert(0,"ayse")                                                                      #
#                                                                                               #
    liste.insert(len(liste),"beren")                                                            #
#                                                                                               #
#################################################################################################
#                                                                                               #
#           pop() metodu                                                                        #
#                                                                                               #
#   eleman siler                                                                                #
#                                                                                               # 
    liste.pop(0)                                                                                #
    liste.pop(4)                                                                                #
#                                                                                               #
#################################################################################################
#                                                                                               #
#           count() metodu                                                                      #
#                                                                                               #
#  eleman�n ka� tane oldu�unu verir                                                             #
    liste.count("arif")                                                                         #
    liste.count("ayse")                                                                         #    
#                                                                                               #
#################################################################################################
#                                                                                               #
#           copy() metodu                                                                       #
#                                                                                               #
#   mevcut listeyi kopyalar                                                                     #
#                                                                                               #   
    liste_yedek=liste.copy()                                                                    #
#                                                                                               #
################################################################################################# 
#                                                                                               #    
#           #extend() metodu                                                                    #
#                                                                                               #
#   iki listeyi birle�tirir.                                                                    #
#                                                                                               #
    liste.extend(["a","b",10])                                                                  #
#                                                                                               #
#################################################################################################
#                                                                                               #    
#           index() metodu                                                                      #
#                                                                                               #
#   bir eleman�n hangi indexte oldu�unu verir                                                   # 
#                                                                                               #    
    liste.index("ayse")                                                                         #
#                                                                                               #
#################################################################################################   
#                                                                                               #
#       reverse() metodu                                                                        #
#                                                                                               #    
#    elemanlar� ters s�ralar                                                                    #
#                                                                                               #    
    liste.reverse()                                                                             #
#                                                                                               #
#################################################################################################
#                                                                                               #
#           sort() metodu                                                                       #
#                                                                                               #    
#    listeyi s�ralar                                                                            #
# ayn� t�r elemanlar yoksa hata verir.                                                          #
#                                                                                               #
    liste1=[50,20,30]                                                                           #
    liste2=["k","b","c"]                                                                        #
#                                                                                               #   
    liste1.sort()                                                                               #
    liste2.sort()                                                                               #
#                                                                                               #    
#################################################################################################  
#           clear() metodu                                                                      #
#                                                                                               #    
#   listeyi temizler                                                                            #
#                                                                                               #
    liste1.clear()                                                                              #
    liste2.clear()                                                                              #
#                                                                                               #
#################################################################################################













#################################################################################################
#                                                                                               #
#                                   ------> Demetler (Tuples) <------                           #
#                                                                                               #
#                                                                                               #
#       Listelerden �nemli fark�, de�i�tirilemez olmas�d�r.                                     #
#       S�ral�d�r.                                                                              #
#       Kapsay�c�d�r.                                                                           #
#                                                                                               #
#                                                                                               #
    tuple1=("ali","veli",1,2,3.2,[1,2,3,4])                                                     #
#                                                                                               #
    tuple2="ali","veli",1,2,3.2,[1,2,3,4]                                                       #
#                                                                                               #
#       tupleler tek elemanl� olursa string olur. bu y�zden sona virg�l atmak gerekir.          #
    tuple3=("eleman",)                                                                          #
#                                                                                               #
#                                                                                               #
#                                                                                               #
#           Eleman ��lemleri                                                                    #
#                                                                                               #    
#                                                                                               #
    tuple4=("ali","veli",1,2,3,[1,2,3,4])                                                       #
#                                                                                               #
    tuple4[0]                                                                                   #
#                                                                                               #
    tuple4[0:2]                                                                                 #
#                                                                                               #
#################################################################################################
    
    
    
    
    
    
    
    
    
    
    
    

####################################################################################################
#                                                                                                  #
#                                   ------> S�zl�k (Dictionary) <------                           #
#                                                                                                  #
#                                                                                                  #
#       Kapsay�c�d�r.                                                                              #
#       S�ras�zd�r.                                                                                #
#       De�i�tirilebilirdir.                                                                       #
#       Anahtar ifadeler(key) ve kar��l�klar�n�n (value) bir arada tutuldu�u veri yap�s�d�r.       #
#       Listelerdeki gibi indexleme i�lemleri yap�lamaz.                                           #
#       S�zl�klerdeki key de�erleri "sabit veri yap�lar�yla" olu�turulabilir.                      #
#                                                                                                  #
    sozluk1={"REG":"Regresyon Modeli",                                                             #
            "LOJ":"Lojistik Regresyon",                                                            #
            "CART":"Classification and Reg"}                                                       #
#                                                                                                  #
    len(sozluk1)                                                                                   #
#                                                                                                  #
    sozluk2={                                                                                      #
            "REG":10,                                                                              #
            "LOJ":20,                                                                              #
            "CART":30                                                                              #
            }                                                                                      #
#                                                                                                  #
    sozluk3={                                                                                      #
            "REG":["RMSE",10],                                                                     #
            "LOJ":["MSE",20],                                                                      #
            "CART":["SSE",30]                                                                      #
            }                                                                                      #
#                                                                                                  #
#                                                                                                  #
#       S�zl�k elemanlar�na eri�me                                                                 #
#                                                                                                  #
    sozluk1["REG"]                                                                                 #
    sozluk2["REG"]                                                                                 #
    sozluk3["REG"]                                                                                 #
#                                                                                                  #
#       S�zl�k i�inde s�zl�k �rne�i                                                                #
#                                                                                                  #
    sozluk4={"REG":{                                                                               #
                    "RMSE":10,                                                                     #
                    "MSE":20,                                                                      #
                    "SSE":30                                                                       #
                    },                                                                             #
                                                                                                   #
            "LOJ":{                                                                                #
                    "RMSE":40,                                                                     #
                    "MSE":50,                                                                      #
                    "SSE":60                                                                       #
                    },                                                                             #
                                                                                                   #
            "CART":{                                                                               #
                    "RMSE":70,                                                                     #
                    "MSE":80,                                                                      #
                    "SSE":90                                                                       #
                    }                                                                              #
            }                                                                                      #
#                                                                                                  #
    sozluk4["LOJ"]["RMSE"] 
    sozluk4["REG"]["RMSE"]                                                                         #
#                                                                                                  #
#                                                                                                  #
#           Eleman Ekleme/De�i�tirme                                                               #
#                                                                                                  #
#       ekleme                                                                                     #
#                                                                                                  #
    sozluk1["GBM"]="Gradiend Boosting Mac"          
    sozluk4["ARR"]  = {"KKK": 25}                              #
#                                                                                                  #
#       de�i�tirme                                                                                 #
#                                                                                                  #
    sozluk1["REG"]="Coklu Dogrusal Regresyon"                                                      #
#                                                                                                  #
                                                                  #
#                                                                                                  #
    tuple1=("tuple",)                                                                              #
    type(tuple1)                                                                                   #
#                                                                                                  #
    sozluk1[tuple1]="Yeni bir sey"                                                                 #
#                                                                                                  #
####################################################################################################















####################################################################################################
#                                                                                                  #
#                                   ------> K�me (Set) <------                                     #
#                                                                                                  #
#                                                                                                  #
#       S�ras�zd�r.                                                                                #
#       De�erleri e�sizdir. (Tekrar eden de�erlerden olu�amaz)                                     #
#       De�i�tirilebilirdir.                                                                       #
#       Farkl� tipleri bar�nd�rabilir. (Kapsay�c�)                                                 #
#                                                                                                  #
#       Performans odakl�d�r. H�zl�d�r.                                                            #
#                                                                                                  #
#                                                                                                  #
#           Set olu�turma                                                                          #
#                                                                                                  #
    liste=["a","ali",123]                                                                          #
#                                                                                                  #
    kume= set(liste)                                                                               #
#                                                                                                  #
    kume                                                                                           #
    tuple1=("a","ali")                                                                             #
#                                                                                                  #
    kume2= set(tuple1)                                                                             #
#                                                                                                  #
    ali="lutfen_ata_bakma_uzaya_git"                                                               #
    type(ali)                                                                                      #
#                                                                                                  #
    set1=set(ali)                                                                                  #
#                                                                                                  #
    set1                                                                                           #
#                                                                                                  #
    liste2=["ali","lutfen","ata","bakma","uzaya","git","git","ali","git"]                          #
    liste2                                                                                         #
    set2=set(liste2)                                                                               #
    set2                                                                                           #
#                                                                                                  #
    len(set1)                                                                                      #
    len(set2)                                                                                      #
#                                                                                                  #
    liste2[0]                                                                                      #
    set2[0]                                                                                        #
#                                                                                                  #
#                                                                                                  #
#           Eleman Ekleme/��karma                                                                  #
#                                                                                                  #
    liste=["gelecegi","yazanlar"]                                                                  #
#                                                                                                  #
    set1=set(liste)                                                                                #
#                                                                                                  #
#       Ekleme                                                                                     #
#                                                                                                  #
    set1.add("ile")                                                                                #
#                                                                                                  #
    set1.add("gelecege_git")                                                                       #
#                                                                                                  #
    set1.add("ile")                                                                                #
#                                                                                                  #
#           Eleman Silme                                                                           #
#                                                                                                  #
#   e�er set i�inde veri yoksa hata verir.                                                         #
#   set1.remove("ali")                                                                             #
#                                                                                                  # 
#   veri yokken hata ��kar�p durmamas� i�in "discard" kullan�l�r.                                  #
    set1.discard("ali")                                                                            #
#                                                                                                  #
#                                                                                                  #
#           Setlerde ��lemler (K�me ��lemleri)                                                     #
#                                                                                                  #
#                                                                                                  #
#       difference() iki k�men�n fark� ---> "-" ifadesi                                            #
#       intersection() iki k�menin kesi�imi ----> "&" ifadesi                                      #
#       union() iki k�menin birle�imi                                                              #
#       symmetric_difference() ikisinde de olmayanlar                                              #
#                                                                                                  #
    set1=set([1,3,5])                                                                              #
    set2=set([1,2,3])                                                                              #
#                                                                                                  #
#       set1 de olup set2 de olmayan elemanlar� bulur.                                             #
    set1.difference(set2)                                                                          #
    type(set1.difference(set2))                                                                    #
    set2.difference(set1)                                                                          #
#                                                                                                  #
#       ikisinde de olmayanlar                                                                     #
#                                                                                                  #
    set1.symmetric_difference(set2)                                                                #
#                                                                                                  #
    set1-set2                                                                                      #
    set2-set1                                                                                      #
#                                                                                                  #
#                                                                                                  #
#       kesi�imleri                                                                                #
#                                                                                                  #
    set1.intersection(set2)                                                                        #
    set2 & set1                                                                                    #
#                                                                                                  #
    kesisim= set2 & set1                                                                           #
#                                                                                                  #
#                                                                                                  #
#       birle�im                                                                                   #
#                                                                                                  #
    birlesim=set1.union(set2)                                                                      #
#                                                                                                  #
#       set1 in de�erlerini kesi�imdekilerle de�i�tirme                                            #
#                                                                                                  #
    set1.intersection_update(set2)                                                                 #
#                                                                                                  #
#                                                                                                  #
#                                                                                                  #
#           Setlerde Sorgu ��lemleri                                                               #
#                                                                                                  #
#                                                                                                  #
    set1=set([7,8,9])                                                                              #
    set2=set([5,6,7,8,9,10])                                                                       #
#                                                                                                  #
#       iki k�menin kesi�imi bo� mu?                                                               #
#                                                                                                  #
    set1.isdisjoint(set2)                                                                          #
#                                                                                                  #
#                                                                                                  #
#       bir k�menin t�m elemanlar�, ba�ka k�menin i�inde var m�?                                   #
#                                                                                                  #
#       set1, set2'nin alt k�mesi mi demektir.                                                     #
    set1.issubset(set2)                                                                            #
#                                                                                                  #
#       bir k�menin di�er k�meyi kapsay�p kapsamad���?                                             #
#                                                                                                  #
    set2.issuperset(set1)                                                                          #
#                                                                                                  #
####################################################################################################









