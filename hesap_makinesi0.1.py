print("""**************************
HESAP MAKİNESİ
**************************
""")

a= float(input("Birinci Sayı: "))
b= input("İşlem: ")
c= float(input("İkinci Sayı: "))

if b=="+" :
    d = a+c

elif b=="-":
    d = a-c

elif b=="/":
    d = a/c

elif b=="*" or b=="x":
    d = a*c

else:
    print("Geçersiz İşlem..")

a = ((d%1) == 0)
if a :
    d = int(d)

print("İşlem Sonucu: {}".format(d))













