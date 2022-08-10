print("""Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.\n
Solution:""")

c=0
for i in range(999,99,-1):

    for j in range(999,99,-1):
        a = i*j
        b= int(str(a)[::-1])
        if a==b and a>c:
            c = a

print(c)

