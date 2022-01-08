print("Beden Kitle Endeksinizi hesaplamamız için lütfen bilgilerinizi giriniz.")
kilo= float(input("Kilonuz= "))
boy= float(input("Boyunuz(m)= "))
a= str(kilo/boy/boy)
print("Beden Kitle Endeksiniz: {}".format(a[:4]))

