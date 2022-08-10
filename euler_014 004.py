print("""Problem:
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.\n
Solution:""")

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