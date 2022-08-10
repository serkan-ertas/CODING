a = input("Enter a word here: ")

ltrdict = dict()

for i in a:
    if i in ltrdict:
        ltrdict[i] += 1
    else:
        ltrdict[i] = 1

for k,l in ltrdict.items():
    print(f"key: {k} /// value: {l}")