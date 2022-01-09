vize1= float(input("1. Vize Notu: "))
vize2= float(input("2. Vize Notu: "))
final= float(input("Final Notu: "))

ortalama = (vize1*3/10)+(vize2*3/10)+(final*4/10)



a = ((ortalama%1)==0)
if a:
    ortalama = int(ortalama)
else:
    ortalama= str(ortalama)
    ortalama = ortalama[:4]
    ortalama= float(ortalama)


if ortalama>=90:
    print("Ortalamanız: {}\nAA".format(ortalama))
elif ortalama>=85:
    print("Ortalamanız: {}\nBA".format(ortalama))
elif ortalama>=80:
    print("Ortalamanız: {}\nBB".format(ortalama))
elif ortalama>=75:
    print("Ortalamanız: {}\nCB".format(ortalama))
elif ortalama>=70:
    print("Ortalamanız: {}\nCC".format(ortalama))
elif ortalama>=65:
    print("Ortalamanız: {}\nDC".format(ortalama))
elif ortalama>=60:
    print("Ortalamanız: {}\nDD".format(ortalama))
elif ortalama>=55:
    print("Ortalamanız: {}\nFD".format(ortalama))
else:
    print("Ortalamanız: {}\nFF".format(ortalama))






