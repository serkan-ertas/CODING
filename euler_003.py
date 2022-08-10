print("""Problem:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?\n
Solution:""")

def num(int1):
  divisor = 2
  while True:
    if int1 / divisor == 1:
      print(divisor)
      break
    elif int1 % divisor == 0:
      int1 /= divisor
    else:
      divisor += 1

num(600851475143)