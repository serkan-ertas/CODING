print("""****************************
Armstrong Numbers
****************************
Press q to quit the program.
""")

while True:
    a = input("What number you will check if it is a Armstrong Number, or not: ")
    if a == "q" or a == "Q":
        print("\n***************************\nQuitting the program..\n***************************")
        break
    else:
        b = int(a)
        c = int()

        for i in a:
            i = int(i)
            c += (i ** len(a))
        if c == b:
            print(b, "is a Armstrong Number.\n")
        else:
            print(b, "is NOT a Armstrong Number.\n")
