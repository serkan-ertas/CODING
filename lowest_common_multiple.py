def function(number1, number2):
    if number1>number2:
        buyuk = number1
        kucuk = number2
    else:
        buyuk = number2
        kucuk = number1
    for i in range(buyuk, (kucuk*buyuk) +1):
        if (i%buyuk==0) and (i%kucuk==0):
            return i


# function has been defined, its time for program:

while True:
    a= int(input("First Number: "))
    b= int(input("Second Number: "))
    print(function(a,b))