def function():
    liste = list()
    for a in range(1,101):
        for b in range(1,101):
            for c in range(1,101):
                if (a**2)+(b**2)==(c**2) :
                    liste.append((a,b,c))
    return liste

for i in function():
    print(i)
