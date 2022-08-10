def function(number1,number2):
    list1 = []
    list2 = []
    for i in range(1,number1+1):
        if number1%i == 0:
            list1.append(i)
    for i in range(1, number2+1):
        if number2%i == 0:
            list2.append(i)
    list1 = list1[::-1]
    list2 = list2[::-1]
    for i in list1:
        for a in list2:
            if a==i:
                return a
    return 1

#defined the function, now its time for program:

while True:
    b = int(input("First Number: "))
    c = int(input("Second Number: "))
    print(function(b,c))
