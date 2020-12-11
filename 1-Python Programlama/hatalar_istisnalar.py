

a = 10 
b = 0


try:
    print(a/b)

except ZeroDivisionError:
    print("Paydada 0 olamaz")



#tip hatası
    
a = 15
b = "2"


try:
    print(a/b)
    
except TypeError:
    print("Sayılar, sayılarla işleme girer.")