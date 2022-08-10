print("""Problem:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.\n
Solution:""")

done = False
for a in range(1,1000):
    if done:
        break
    for b in range(1,1000-a):
        c = 1000-b-a
        if c*c == b*b + a*a:
            print(a*b*c)
            done = True
            break
