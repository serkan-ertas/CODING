import random

def password(length):    ##you should provide a length to the code
    pw = str()
    for i in range(length):
        pw += random.choice("qwertyuopasdfghjklizxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.12345678901234567890*/")
    print(pw)
