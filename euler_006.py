a = 0
b = 0
for i in range(101):
    a += (i**2)
    b += i
    if i==100:
        b **= 2

print(b-a)