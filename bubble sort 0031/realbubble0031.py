bub=[]
print("Enter list of numbers separated by commas")
inp=input()
lis=inp.split(',')
for a in lis:
    bub.append(int(a))
count=0
j=0

while count < (len(bub)-1):
    count=0
    j=0
    for i in range(0,len(bub)-1):
        j=j+1
        if bub[i] > bub[j]:
            mid=bub[i]
            bub[i]=bub[j]
            bub[j]=mid
            #print(*bub)
        else:
            count=count+1
print(*bub)
