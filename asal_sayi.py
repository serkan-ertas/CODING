def fonksiyon(sayı):

    if sayı==1:
        return False
    elif sayı==2:
        return True
    else:
        for i in range(2,sayı):
            if (sayı%i)==0:
                return False
        return True

#The upper part is the definition part of function
print("""*************************\nPrime Number Program\nPress 'q' to quit\n*************************""")

while True:
    a = input("Number: ")
    if a == "q" or a== "Q":
        print("Programdan çıkılıyor..")
        break
    elif a=="1":
        print("1 asal sayı değildir.")
    elif a=="2":
        print("2 asal sayıdır.")
    else:
        a= int(a)
        if fonksiyon(a):
            print(a,"asal sayıdır.")
        else:
            print(a,"asal sayı değildir.")














