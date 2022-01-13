print("""****************************

Armstrong Sayıları

****************************

Programdan çıkmak için 'q'ya basın.
""")

while True:
    a = input("Hangi sayının Armstrong olup olmadığını kontrol etmek istersiniz: ")
    if a=="q" or a=="Q":
        print("\n***************************\nProgramdan çıkış yapılıyor.\n***************************")
        break
    else:
        b = int(a)
        c = int()

        for i in a:
            i=int(i)
            c += (i**len(a))
        if c==b:
            print(b,"bir Armstrong sayısıdır.")
        else:
            print(b,"bir Armstrong sayısı değildir.")










