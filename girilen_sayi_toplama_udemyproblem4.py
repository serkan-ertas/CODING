toplam= 0

while True:
    a = input("Sayı giriniz: ")

    if a=="q" or a=="Q":
        print("Toplam Değer:",toplam)
        break
    else:
        a= int(a)
        toplam += a