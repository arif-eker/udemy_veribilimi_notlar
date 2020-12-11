#Sayýlar

#int sayý
9

#float sayý
9.2

#Ýþlemler
9*9
9/9
9+9
9-5


#Karakter Dizileri (Stringler)

"Merhaba Dünya"

'Merhaba Dünya'

###########################################################
#                                                         #
#           Bir nesnenin tipini nasýl öðreniriz?          #
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
#       string ifadenin uzunluðunu verir                  #
#                                                         #
#                                 #########################
#                                 #
    gel_yaz="gelecegi_yazanlar"   #
    len(gel_yaz)                  #
#                                 #
###################################



##########################################################
#           upper() & lower() fonksiyonlarý              #
#                                                        #
#                                                        #
#     string ifadeleri büyük/küçük harf þekline çevirir. #
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
#      true/false döner                                 #
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
#   string içindeki harfleri deðiþtirmek için kullanýlýr                                            #
#                                                                                                   #
#   parantez içindeki ilk ifade deðiþtirilmek istenen harf, ikinci ifade ise dönüþtürülecek harftir #
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
#    istenmeyen karakterleri kýrpmak için kullanýlýr. ön taným olarak boþluklarý siler           #
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
                                    #------> Metotlara Genel Bakýþ <------#
                                    #                                     #
                                    #######################################


############################################################
#                   dir() fonksiyonu                       #
#                                                          #
#                                                          #
#  içindeki nesneye uygulanabilecek fonksiyonlarý gösterir #
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
                                   #------> SUBSTRÝNGLER <------#
                                   #                            #
                                   ##############################

####################################################################
#                                                                  #
#elimizdeki stringlerin alt stringlerine ulaþmak için kullanýrýz.  #
#                                                                  #
#                                                                  #
#                                                                  #############
    gel_yaz="gelecegi_yazanlar"                                                #
#                                                                              #
#   0. indeks                                                                  #
    gel_yaz[0]                                                                 #
#                                                                              #
#   0 dan 2 dahil almak için. 0:3 yazmak gerekir. 0 dahil ama 3 dahil deðildir.#
    gel_yaz[0:3]                                                               #
#                                                                              #    
################################################################################



                                   #############################
                                   #                           #
                                   #------> DEÐÝÞKENLER <------#
                                   #                           #
                                   #############################




#Sayýsal Deðiþkenler
type(10)
type(10.2)
type(2+1j)

#String deðiþken
arif="Arif"
Arif='Arif'



                                   #################################
                                   #                               #
                                   #------> Tip Dönüþümleri <------#
####################################                               #
#                                                                  #
#                                                                  #
#       kullanýcýdan alýnan deðerleer default olarak "stringtir"   #
#                                                                  #
        toplama_bir= input()                                       #
        toplama_iki= input()                                       #
#                                                                  #
        type(toplama_bir)                                          #
#                                                                  #
        toplama_bir + toplama_iki                                  #
                                                                   #
#tip dönüþtürmek için baþýna (int) ifadeleri eklenir.              #
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
            print("geleceði","yazanlar")                              #
#                                                                     #
#           _ ile birleþtirmek için                                   #
#                                                                     #
            print("gelecegi","yazanlar",sep="_")                      #
#                                                                     ###############################
#                                                                                                   #
#                                                                                                   #
#                                                                                                   #
#           sep bir argümandýr.                                                                     #
#           fonksiyonlarýn argümanlarýnýn nasýl kullanýlacaðýný bilmek için baþlarýna               #
#           soru iþareti getirmek gerekir : ?print ifadesi yazýp çalýþtýrýnca bilgi verecektir.     #
#                                                                                                   #
#####################################################################################################

#****************************************************************************************************************************#
            
#****************************************************************************************************************************#
            
#****************************************************************************************************************************#
                 
                                    ###########################################
                                    #                                         #
                                    #       ------> VERÝ YAPILARI <------     #
                                    #                                         #
                                    ###########################################

#################################################################################################
#                                                                                               #
#                                   ------> Listeler <------                                    #
#                                                                                               #
#                                                                                               #
#       Sýralýdýr.                                                                              #
#       Deðiþtirilebilirdir.                                                                    #
#       Kapsayýcýdýr (Farklý tipte verileri tutabilir)                                          #
#                                                                                               #
#       [] veya list() þeklinde oluþturulabilir.                                                #
#                                                                                               #
#           liste oluþturma                                                                     #
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
#           liste içi tip sorgulama                                                             #
#                                                                                               #
    type(list_genis[0])                                                                         #
#                                                                                               #
#           iki listeyi birleþtirme                                                             #
    tum_liste=[liste,list_genis]                                                                #
#                                                                                               #
#           listeyi silme                                                                       #
#                                                                                               #
    del tum_liste                                                                               #
#                                                                                               #
#daha sonra bunu yorum satýrýna al                                                              #
#                                                                                               #
#                                                                                               #
#           liste elemanlarýna eriþmek                                                          #
#                                                                                               #
    yeni_liste=[10,20,30,40,50]                                                                 #
#                                                                                               #
    yeni_liste[0:2]                                                                             #
    yeni_liste[:2]                                                                              #
    yeni_liste[2:]                                                                              #
#                                                                                               #
    baska_liste=["a",10,[20,30,40,50]]                                                          #
#                                                                                               #
#           liste içindeki liste elemanýna eriþmek için:                                        #
#                                                                                               #
    baska_liste[2][1]                                                                           #
#                                                                                               #
#yani listenin 2. elamanýnýn 1. elamanýna eriþ.                                                 #
#                                                                                               #      
#################################################################################################
#                                                                                               #
#           listelere eleman ekleme/deðiþtirme/silme                                            #  
#                                                                                               #      
#       Eleman Deðiþtirme                                                                       #
#                                                                                               #
    liste=["ali","veli","berkcan","ayse"]                                                       #
#                                                                                               #
    liste[0:3]="alinin_babasi","velinin_babasi","berkcanin_babasi"                              #
#                                                                                               #    
#################################################################################################    
#       Eleman Ekleme                                                                           #
#   Bu þekilde atama yapmadan ekleme yapýldýðýnda, kemal listeye kalýcý olarak eklenmez.        #
#   bunun için atama yapmak gerekir.                                                            #
#                                                                                               #   
    liste +["kemal"]                                                                            #
    liste=liste+["kemal"]                                                                       #
#                                                                                               #    
#################################################################################################    
#       Eleman Silme                                                                            #  
#                                                                                               #
#  indeksteki elemaný silmek                                                                    #
    del liste[2]                                                                                #
#                                                                                               #    
#################################################################################################
#                                   ------> Liste Metotlarý <------                             #
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
#  elemanýn kaç tane olduðunu verir                                                             #
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
#   iki listeyi birleþtirir.                                                                    #
#                                                                                               #
    liste.extend(["a","b",10])                                                                  #
#                                                                                               #
#################################################################################################
#                                                                                               #    
#           index() metodu                                                                      #
#                                                                                               #
#   bir elemanýn hangi indexte olduðunu verir                                                   # 
#                                                                                               #    
    liste.index("ayse")                                                                         #
#                                                                                               #
#################################################################################################   
#                                                                                               #
#       reverse() metodu                                                                        #
#                                                                                               #    
#    elemanlarý ters sýralar                                                                    #
#                                                                                               #    
    liste.reverse()                                                                             #
#                                                                                               #
#################################################################################################
#                                                                                               #
#           sort() metodu                                                                       #
#                                                                                               #    
#    listeyi sýralar                                                                            #
# ayný tür elemanlar yoksa hata verir.                                                          #
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
#       Listelerden önemli farký, deðiþtirilemez olmasýdýr.                                     #
#       Sýralýdýr.                                                                              #
#       Kapsayýcýdýr.                                                                           #
#                                                                                               #
#                                                                                               #
    tuple1=("ali","veli",1,2,3.2,[1,2,3,4])                                                     #
#                                                                                               #
    tuple2="ali","veli",1,2,3.2,[1,2,3,4]                                                       #
#                                                                                               #
#       tupleler tek elemanlý olursa string olur. bu yüzden sona virgül atmak gerekir.          #
    tuple3=("eleman",)                                                                          #
#                                                                                               #
#                                                                                               #
#                                                                                               #
#           Eleman Ýþlemleri                                                                    #
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
#                                   ------> Sözlük (Dictionary) <------                           #
#                                                                                                  #
#                                                                                                  #
#       Kapsayýcýdýr.                                                                              #
#       Sýrasýzdýr.                                                                                #
#       Deðiþtirilebilirdir.                                                                       #
#       Anahtar ifadeler(key) ve karþýlýklarýnýn (value) bir arada tutulduðu veri yapýsýdýr.       #
#       Listelerdeki gibi indexleme iþlemleri yapýlamaz.                                           #
#       Sözlüklerdeki key deðerleri "sabit veri yapýlarýyla" oluþturulabilir.                      #
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
#       Sözlük elemanlarýna eriþme                                                                 #
#                                                                                                  #
    sozluk1["REG"]                                                                                 #
    sozluk2["REG"]                                                                                 #
    sozluk3["REG"]                                                                                 #
#                                                                                                  #
#       Sözlük içinde sözlük örneði                                                                #
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
#           Eleman Ekleme/Deðiþtirme                                                               #
#                                                                                                  #
#       ekleme                                                                                     #
#                                                                                                  #
    sozluk1["GBM"]="Gradiend Boosting Mac"          
    sozluk4["ARR"]  = {"KKK": 25}                              #
#                                                                                                  #
#       deðiþtirme                                                                                 #
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
#                                   ------> Küme (Set) <------                                     #
#                                                                                                  #
#                                                                                                  #
#       Sýrasýzdýr.                                                                                #
#       Deðerleri eþsizdir. (Tekrar eden deðerlerden oluþamaz)                                     #
#       Deðiþtirilebilirdir.                                                                       #
#       Farklý tipleri barýndýrabilir. (Kapsayýcý)                                                 #
#                                                                                                  #
#       Performans odaklýdýr. Hýzlýdýr.                                                            #
#                                                                                                  #
#                                                                                                  #
#           Set oluþturma                                                                          #
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
#           Eleman Ekleme/Çýkarma                                                                  #
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
#   eðer set içinde veri yoksa hata verir.                                                         #
#   set1.remove("ali")                                                                             #
#                                                                                                  # 
#   veri yokken hata çýkarýp durmamasý için "discard" kullanýlýr.                                  #
    set1.discard("ali")                                                                            #
#                                                                                                  #
#                                                                                                  #
#           Setlerde Ýþlemler (Küme Ýþlemleri)                                                     #
#                                                                                                  #
#                                                                                                  #
#       difference() iki kümenün farký ---> "-" ifadesi                                            #
#       intersection() iki kümenin kesiþimi ----> "&" ifadesi                                      #
#       union() iki kümenin birleþimi                                                              #
#       symmetric_difference() ikisinde de olmayanlar                                              #
#                                                                                                  #
    set1=set([1,3,5])                                                                              #
    set2=set([1,2,3])                                                                              #
#                                                                                                  #
#       set1 de olup set2 de olmayan elemanlarý bulur.                                             #
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
#       kesiþimleri                                                                                #
#                                                                                                  #
    set1.intersection(set2)                                                                        #
    set2 & set1                                                                                    #
#                                                                                                  #
    kesisim= set2 & set1                                                                           #
#                                                                                                  #
#                                                                                                  #
#       birleþim                                                                                   #
#                                                                                                  #
    birlesim=set1.union(set2)                                                                      #
#                                                                                                  #
#       set1 in deðerlerini kesiþimdekilerle deðiþtirme                                            #
#                                                                                                  #
    set1.intersection_update(set2)                                                                 #
#                                                                                                  #
#                                                                                                  #
#                                                                                                  #
#           Setlerde Sorgu Ýþlemleri                                                               #
#                                                                                                  #
#                                                                                                  #
    set1=set([7,8,9])                                                                              #
    set2=set([5,6,7,8,9,10])                                                                       #
#                                                                                                  #
#       iki kümenin kesiþimi boþ mu?                                                               #
#                                                                                                  #
    set1.isdisjoint(set2)                                                                          #
#                                                                                                  #
#                                                                                                  #
#       bir kümenin tüm elemanlarý, baþka kümenin içinde var mý?                                   #
#                                                                                                  #
#       set1, set2'nin alt kümesi mi demektir.                                                     #
    set1.issubset(set2)                                                                            #
#                                                                                                  #
#       bir kümenin diðer kümeyi kapsayýp kapsamadýðý?                                             #
#                                                                                                  #
    set2.issuperset(set1)                                                                          #
#                                                                                                  #
####################################################################################################









