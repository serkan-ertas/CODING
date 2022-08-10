print("""Problem:
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?\n
Solution:""")

import math

num=1
i=20
for i in range(2,20):
    if num%i != 0:
        num *= int((i/math.gcd(num,i)))

print(num)