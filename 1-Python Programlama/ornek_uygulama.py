
sinir = 50000



magaza_adi=input("Mağaza adı nedir?")

gelir=int(input("Mağaza gelirini giriniz... : "))

if gelir>sinir:
    print("Tebrikler: "+magaza_adi+ " promosyon kazandınız.")
elif gelir<sinir:
    print("Uyari! Düşük gelir : "+ str(gelir))
else:
    print("Takibe devam...")