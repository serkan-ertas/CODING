import random

import time


print("""*****************************

 Number Finding Game

·Numbers are between 1 and 40
·You have 6 attempts
·Press 'q' to quit

*****************************
""")

toplam = 7
a= -100
while True:

    while True:
        if toplam==7:
            break
        else:
            a = int(input("Num: "))
            break

    if a=="q" or a=="Q":
        break

    else:
        a= int(a)

        if toplam==0:
            toplam = 7
            time.sleep(1)
            print("You have failed, the number was",b)

        elif toplam==7:
            b = random.randint(1,40)
            toplam -= 1

        elif a==b:
            time.sleep(1)
            print("Correct!")
            toplam=7

        elif a>b:
            time.sleep(1)
            toplam -= 1
            print("Less,",toplam,"attempts remain")

        elif b>a:
            time.sleep(1)
            toplam -= 1
            print("More,",toplam,"attempts remain")






