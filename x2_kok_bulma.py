print(
    "Denklem ax'2 + bx + c şeklinde olacaktır. Lütfen programın işlemini yerine getirebilmesi için bilgileri giriniz.")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
deltakoku = ((b ** 2) - (4 * a * c)) ** 0.5
kok1 = (-b + deltakoku) / (2 * a)
kok2 = (-b - deltakoku) / (2 * a)
print("{}x^2 + {}x + {} formülündeki kökler:".format(a , b , c))
print("1. kök: {} \n2. kök: {}".format(kok1 , kok2))
