c=0
for i in range(999,99,-1):

    for j in range(999,99,-1):
        a = i*j
        b= int(str(a)[::-1])
        if a==b and a>c:
            c = a

print(c)

