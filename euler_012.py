def divisor_check(x):
    a = 0
    for i in range(1,int((x**0.5))+1):
        if not x%i:
            a += 1
    if a*2 >= 500:
        return True
    else:
        return False
n=1
while True:
    num = (n*(n+1))/2
    if divisor_check(num):
        print(num)
        break
    n+=1