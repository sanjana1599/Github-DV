powlist=[]

for a in range(2,101):
    for b in range(2,101):
        pow=a**b
        if pow in powlist:
            continue
        else:
            powlist.append(pow)
print(len(powlist))
