import math

num=1
i=20
for i in range(2,20):
    if num%i != 0:
        num *= int((i/math.gcd(num,i)))

print(num)