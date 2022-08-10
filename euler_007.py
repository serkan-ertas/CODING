print("""Problem:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?\n
Solution:""")

def prime_check(x):
    for i in range(2,int(x**0.5)+1):
        if not x%i:
            return False
    return True

d=0
primes=1

while d<10001:
    primes += 1
    if prime_check(primes):
        d += 1

print(primes)


