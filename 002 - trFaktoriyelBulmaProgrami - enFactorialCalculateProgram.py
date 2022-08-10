print("""***************************

Faktöriyel Bulma Programı

***************************

Programdan çıkmak için 'q' ya basın.
""")


while True:

    a = input("Faktöriyelini bulmak istediğiniz sayıyı giriniz: ")
    b = 1

    if a == "Q" or a=="q":
        print("\nProgramdan çıkılıyor..")
        break
    else:
        a=int(a)
        if a==1 or a==0:
            print("{}! = 1".format(a))

        elif a<=0:
            print("Negatif sayıların faktöriyeli hesaplanamaz!")

        else:
            for i in range(2,a+1):
                b *= i
            print("{}! = {}".format(a,b))












