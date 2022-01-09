sekil = input("Üçgenin mi Dörtgenin mi? ")

if sekil=="Üçgen" or sekil=="üçgen":
    a = int(input("1. Kenar: "))
    b = int(input("2. Kenar: "))
    c = int(input("3. Kenar: "))
    if ((a+b>c) and (abs(a-b)<c)) and ((c+b>a) and (abs(c-b)<a)) and ((a+c>b) and (abs(a-c)<b)):
        if a==b and a==c:
            print("Eşkenar Üçgen")
        elif a!=b and a!=c and b!=c:
            print("Çeşitkenar Üçgen")
        else:
            print("İkizkenar Üçgen")
    else:
        print("Girdiğiniz uzunluktaki kenarlardan bir üçgen oluşturulamaz.")

elif sekil=="Dörtgen" or sekil=="dörtgen":
    a = int(input("1. Kenar: "))
    b = int(input("2. Kenar: "))
    c = int(input("3. Kenar: "))
    d = int(input("4. Kenar: "))
    if a==b and b==c and c==d:
        print("Kare")
    elif a==c and b==d:
        print("Dikdörtgen veya Paralelkenar")
    else:
        print("Sıradan Bir Dörtgen")