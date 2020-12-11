#           Yan Etkisiz Fonksiyonlar (Pure Functions)


# Örnek 1 : Yan Etki

A = 5

def impure_sum(b):
    return b+A


def pure_sum(a,b):
    return a+b


# Örnek 2 : Ölümcül Yan Etkiler
    

#           İsimsiz Fonksiyonlar (Anonymous Functions)
    
def old_sum(a,b):
    return a+b


old_sum(4,5)


new_sum = lambda a,b : a+b


new_sum(4,5)


sirasiz_liste=[('b',3),('a',8),('d',12),('c',1)]


sorted(sirasiz_liste, key= lambda x: x[1])




#           Vektörel Operasyonlar

a=[1,2,3,4]

b=[2,3,4,5]

ab=[]

range(0,len(a))

#böyle olur ama yapmamalı
for i in range(0,len(a)):
    
    ab.append(a[i]*b[i])


ab



import numpy as np

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])


a*b



#           map & filter & reduce

liste = [1,2,3,4,5]

#   map fonksiyonu, verilen bir nesnenin (vektör) üstünde belirli bir fonksiyonu çalıştırma imkanı verir.

list(map(lambda x: x*10,liste))


#   filter fonksiyonu , iteratif bir nesne alır, bu nesne üzerinden başka bir iteratif nesne oluşturulur. 
#   Ve iteratif nesne içerisinde aradığı şartın sağlandığı tüm elemanlar listelenir.

liste2 = [1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2 == 0, liste2))


#   reduce fonksiyonu, indirgeme işlemi yapar.

from functools import reduce

liste3 = [1,2,3,4]

reduce(lambda a,b: a+b, liste3)





