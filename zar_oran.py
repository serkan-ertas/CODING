from random import choice

numsdic = {1 : 0, 2 : 0, 3 : 0 , 4 : 0 , 5 : 0, 6 : 0}
numslist = [1,2,3,4,5,6]
for i in range(1000000):
    numsdic[choice(numslist)] += 1





for i in numsdic:
    print(numsdic[i])