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
        break

    else:
        a= int(a)
        if fonksiyon(a):
            print(a,"is a prime number.")
        else:
            print(a,"is not a prime number.")














