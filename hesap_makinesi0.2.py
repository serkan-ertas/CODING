import math

print("""***************
   CALCULATOR
***************
press q to quit""")

help(math)

while True:
    print("""
    *******************************
    İŞLEMLER:
    
    1- Toplama                             2- Çıkarma                            3- Bölme
    4- Çarpma                              5- Karekök                            6- Radyan Cinsinden Dereceye Döndür
    7- Derece Cinsinden Radyana Döndür     8- Sinüs                              9- Kosinüs
    10- Tanjant                            11- Kotanjant                         12- ARC COS
    13- ARC SIN                            14- ARC TAN                           15- ARC COT              
    16- Logaritma                          17- İki Dik Kenardan Hipotenüs Bulma  18- Faktöriyel
    19- Sayı Yuvarlama                     20- EBOB                              21- EKOK
    *******************************
    """)
    a= input("İşlem: ")
    if a=="q" or a=="Q":
        print("Calculator sonlandırılıyor..")
    else:
        a = int(a)
        if a == 1:
            print("Toplam İşlemi")
            num1 = int(input("1. Sayı: "))
            num2 = int(input("2. Sayı: "))
            print("Toplam:",num1+num2)

        elif a==2:
            print("Çıkarma İşlemi\n1. Sayı - 2. Sayı")
            num1 = int(input("1. Sayı: "))
            num2 = int(input("2. Sayı: "))
            print(num1-num2)

        elif a==3:
            print("Bölme İşlemi\n1. sayı / 2. sayı")
            num1 = int(input("1. Sayı: "))
            num2 = int(input("2. Sayı: "))
            print(num1/num2)

        elif a==4:
            print("Çarpma İşlemi")
            num1 = int(input("1. Sayı: "))
            num2 = int(input("2. Sayı: "))
            print("Çarpım:",num1*num2)

        elif a==5:
            print("Karekök İşlemi")
            num1 = int(input("Number: "))
            print(math.sqrt(num1))

        elif a==6:
            print("Radyan Cinsinden Dereceye Döndürme")
            num1 = float(input("Radyan: "))
            print(math.degrees(num1))

        elif a==7:
            print("Dereceden Radyan Cinsine Döndürme")
            num1= int(input("Derece: "))
            print(math.radians(num1))

        elif a==8:
            print("Sinüs İşlemi")
            num1 = int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.sin(num1))

        elif a==9:
            print("Kosinüs İşlemi")
            num1 = int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.cos(num1))

        elif a==10:
            print("Tanjant İşlemi")
            num1 = int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.tan(num1))

        elif a==11:
            print("Kotanjant İşlemi")
            num1 = int(input("Derece: "))
            num1 = math.radians(num1)
            print(1/(math.tan(num1)))

        elif a==12:
            print("Arccos İşlemi")
            num1= int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.acos(num1))

        elif a==13:
            print("Arcsin İşlemi")
            num1= int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.asin(num1))

        elif a==14:
            print("Arctan İşlemi")
            num1= int(input("Derece: "))
            num1 = math.radians(num1)
            print(math.atan(num1))

        elif a==15:
            print("Arccot İşlemi")
            num1= int(input("Derece: "))
            num1 = math.radians(num1)
            print(1/(math.atan(num1)))


        elif a==16:
            print("""Logaritma İşlemi""")
            num1= int(input("Log Tabanı: "))
            num2= int(input("Logaritma Alınacak Sayı: "))
            print(math.log(num2,num1))

        elif a==17:
            print("Hipotenüs Bulma")
            num1= int(input("1. Kenar: "))
            num2= int(input("2. Kenar: "))
            print(math.hypot(num1,num2))

        elif a==18:
            print("Faktöriyel İşlemi")
            num1=int(input("Sayı: "))
            print(math.factorial(num1))

        elif a==19:
            print("Ondalık Yuvarlama")
            num1= float(input("Sayı: "))
            if num1%1>=5:
                print(math.ceil(num1))
            else:
                print(math.floor(num1))

        elif a==20:
            print("EBOB İşlemi")
            num1= int(input("1. Sayı: "))
            num2= int(input("2. Sayı: "))
            print(math.gcd(num1,num2))

        elif a==21:
            print("EKOK İşlemi")
            num1= int(input("1. Sayı: "))
            num2= int(input("2. Sayı: "))
            print(math.lcm(num1,num2))

        else:
            print("Geçersiz İşlem")