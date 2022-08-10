print("""Problem:
The sum of the squares of the first ten natural numbers is,
The square of the sum of the first ten natural numbers is,
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.\n
Solution:""")

a = 0
b = 0
for i in range(101):
    a += (i**2)
    b += i
    if i==100:
        b **= 2

print(b-a)