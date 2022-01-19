done = False
for a in range(1,1000):
    if done:
        break
    for b in range(1,1000-a):
        c = 1000-b-a
        if c*c == b*b + a*a:
            print(a*b*c)
            done = True
            break
