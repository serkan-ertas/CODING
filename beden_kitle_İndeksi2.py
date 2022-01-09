print("""***********************
BEDEN KİTLE İNDEKSİ PROGRAMI
***********************""")

kilo= int(input("Kilo: "))
boy= float(input("Boy(m): "))

bki= kilo/(boy**2)
bki=str(bki)
bki= bki[:4]
bki= float(bki)

if bki>=30:
    print("Beden kitle indeksiniz: {}\nObezsiniz.".format(bki))
elif 25<=bki and 30>bki:
    print("Beden kitle indeksiniz: {}\nFazla kilolusunuz.".format(bki))
elif 18.5<=bki and bki<25:
    print("Beden kitle indeksiniz: {}\nNormalsiniz.".format(bki))
else:
    print("Beden kitle indeksiniz: {}\nZayıfsınız.".format(bki))

