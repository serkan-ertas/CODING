print("""*************************************

FİBONACCİ SERİSİ

**********************************

Operations:
1. Write the series up to there including the entered number
2. Finding which element of the array the entered number is
3. Press q to quit the program

""")

while True:
    c = input("Which operation would you like to perform: ")
    liste = [1, 1]
    b = 1

    if c == "q" or c == "Q":
        print("Quitting the program...")
        break


    elif c == "1":

        a = input("How many elements do you want to print: ")
        if a == "q" or a == "Q":
            print("\n***************************\nQuitting the program...\n***************************")
            break
        else:
            a = int(a)
            if a == 1:
                print("[1]")
                continue
            elif a == 2:
                print("[1,1]")
                continue

        for i in liste:
            liste.append(liste[b - 1] + liste[b])
            b += 1
            if a <= len(liste):
                print(liste)
                break

    elif c == "2":

        a = input("Which element of the array you want to find out: ")
        if a == "q" or a == "Q":
            print("Quitting the program...")
            break
        elif a == "1" or a == "2":
            print("1")
            continue
        else:
            a = int(a)

        for i in liste:
            liste.append(liste[b - 1] + liste[b])
            b += 1
            if len(liste) >= a:
                print(liste[a - 1])
                break
