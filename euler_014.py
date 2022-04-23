dicti = {}

def islem(x):

    if not x%2:

        return x/2
    else:
        return 3*x +1

def step(x):
    a=1
    x2=0
    while x!=1:

        if x in dicti:
            x2= a+dicti[x]-1

            break
        x=islem(x)
        a += 1
    if x2 !=0:
        return x2
    else:
        return a

max_a = 0
largnum= 0

for i in range(2,1000000):

    dicti[i]=step(i)

    if step(i) > max_a:
        max_a = step(i)
        largnum= i

print(largnum)