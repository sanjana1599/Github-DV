num=[]
rep=[]
print("Enter numbers")
inp=input()
lis=inp.split(' ')
for a in lis:
    if a not in num:
        num.append(a)
    else: #for all repeat numbers
        if a not in rep: #to not print repeat numbers more than once, even if they are repeated more than twice
            rep.append(a)
print(*rep)
