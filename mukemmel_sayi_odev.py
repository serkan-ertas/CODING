def function(number):
    total = 0
    for i in range(1,number):
        if number%i == 0:
            total += i
    return total

while True:
    a = int(input("Number: "))

    if function(a) == a:
        print("yes")
    else:
        print("no")