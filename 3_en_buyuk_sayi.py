bir= int(input("1. Sayı: "))
iki= int(input("2. Sayı: "))
uc= int(input("3. Sayı: "))

if bir>iki and bir>uc:
    print("En büyük sayı: {}".format(bir))
elif iki>bir and iki>uc:
    print("En büyük sayı: {}".format(iki))
else:
    print("En büyük sayı: {}".format(uc))