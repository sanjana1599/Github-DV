import random
lis=[]
while len(lis) < 5:
    r=random.randint(0,101)
    if r not in lis:
        lis.append(r)
print(*lis)
