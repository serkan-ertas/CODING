print("""Problem:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.\n
Solution:""")

def prime_check(x):
    for i in range(2,int((x**0.5))+1):
        if not x%i:
            return False
    return True

total=2

for i in range(3,2000000,2):
    if prime_check(i):
        total += i

print(total)