from time import time
start = time()
from math import sqrt

def isPrime(n):

    for i in range(2, int(sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True

def isPermutation(num1, num2, num3):

    if set(filter(str.isalnum, str(num1))) == set(filter(str.isalnum, str(num2))) and set(filter(str.isalnum, str(num1))) == set(filter(str.isalnum, str(num3))):
        return True
    else:
        return False

def isFour(num1, num2, num3):
    if len(str(num1)) == 4 and len(str(num2)) == 4 and len(str(num3)) == 4 :
        return True
    else:
        return False

listofnum = list()

for number1 in range(1001,9999,2):
    if isPrime(number1):
        for i in range(2, (10000-number1), 2):
            if isPermutation(number1,(number1+i), (number1+ (2*i))) and isFour(number1, (number1+i), (number1 + (2*i))) and isPrime(number1+i) and isPrime(number1 + (2*i)):
                listofnum.append([number1, (number1+i), (number1 + (2*i))])

print(listofnum)
end = time()

print(end-start)