pali=[]
count=0
y=0
for i in range(100,1000):
    for j in range(i,1000):
        p=i*j
        s=""
        for a in str(p):
            s=a+s
        if s == str(p):
            pali.append(p)

while count < (len(pali)-1):
    count=0
    y=0
    for x in range(len(pali)-1):
        y=y+1
        if pali[x] > pali[y]:
            mid=pali[x]
            pali[x]=pali[y]
            pali[y]=mid
        else:
            count=count+1
print(pali[-1])
