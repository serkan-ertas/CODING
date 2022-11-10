import random
import string

def password(length):    ##you should provide a length to the code
    pw = str()
    for i in range(length):
        pw += random.choice(string.ascii_letters + string.digits*2 + string.punctuation[:10])
    return(pw)