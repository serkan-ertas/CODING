a = input("Enter the word here: ")
b = ""

for i in a:
    if i == "a":
        b += "A"
        continue
    b += i

print(b)