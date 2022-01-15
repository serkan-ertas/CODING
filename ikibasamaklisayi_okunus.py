def function(sayı):
    list1 = ["", " bir", " iki"," üç"," dört"," beş"," altı"," yedi"," sekiz"," dokuz"]
    list10 = ["", "on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]
    birler= sayı%10
    onlar= sayı//10

    return list10[onlar] + list1[birler]
while True:
    a = int(input("Number: "))
    if a =="q" or a=="Q":
        break
    else:
        print(function(a))