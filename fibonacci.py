print("""*************************************

FİBONACCİ SERİSİ

**********************************

İşlemler:
1. Girilen sayı dahil oraya kadar seriyi yazma
2. Girilen sayının dizinin hangi elemanı olduğunu bulma
3. Programdan çıkmak için 'q' ya basın

""")



while True:
    c = input("Kaçıncı işlemi gerçekleştirmek istersiniz: ")
    liste = [1,1]
    b = 1

    if c=="q" or c=="Q":
        print("Programdan çıkılıyor..")
        break


    elif c=="1":

        a = input("Kaçıncı elemana kadar yazdırmak istiyorsunuz: ")
        if a== "q" or a=="Q":
            print("\n***************************\nProgram sonlandırılıyor..\n***************************")
            break
        else:
            a = int(a)
            if a==1:
                print("[1]")
                continue
            elif a==2:
                print("[1,1]")
                continue

        for i in liste:
            liste.append(liste[b-1]+liste[b])
            b += 1
            if a <= len(liste):
                print(liste)
                break

    elif c=="2":

        a = input("Dizinin kaçıncı elemanını bulmak istersiniz: ")
        if a=="q" or a=="Q":
            print("Programdan çıkılıyor..")
            break
        elif a=="1" or a=="2":
            print("1")
            continue
        else:
            a= int(a)

        for i in liste:
            liste.append(liste[b-1]+liste[b])
            b += 1
            if len(liste)>=a:
                print(liste[a-1])
                break

















