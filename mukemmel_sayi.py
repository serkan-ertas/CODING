print(""""**************************************************************
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
Örnek olarak 6 sayısı: [ 1 + 2 + 3 = 6 ]
Programdan çıkmak için 'q' ya basın.
**************************************************************
""")

while True:
    a=input("Mükemmelliğini test edeceğiniz sayı: ")
    if a=="q" or a=="Q":
        print("\n************************\nProgram Sonlandırılıyor.\n************************")
        break
    elif int(a)<=0:
        print("0 veya negatif sayılarda Mükemmellik aranmaz.")
        continue
    else:
        a = int(a)
        liste = list()
        b = 0

        for i in range(1,a):
            liste.append(i)

        for i in liste:
            if a%i == 0:
                b += i

        if b == a:
            print("{} sayısı Mükemmel bir sayıdır.".format(b))

        else:
            print("{} sayısı Mükemmel bir sayı değildir.".format(a))



















