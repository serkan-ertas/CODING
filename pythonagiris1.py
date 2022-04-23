
a = 1
b = 3
c = 0
while a < 100000:
    valid = True
    for i in range(2,(int(b**0.5)+1)):
        if b%i == 0 :
            b += 1
            valid = False
            break
    if valid:
        a += 1
        if str(b)[0] == "3" and str(b)[len(str(b))-1] == "7":
            c += 1
        b += 1
print(c)


k = 0
for i in range(100,1000):
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        k +=1
print(k)