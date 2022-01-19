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


