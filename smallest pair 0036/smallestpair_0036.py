lis=[]
mid=0
count=0
print("Enter 10 integers")
x=input()
s=x.split(' ')

for a in s:
    lis.append(int(a))

while count < (len(lis)-1):
    count=0
    j=0
    for i in range(len(lis)-1):
        j=j+1
        if lis[i] > lis[j]:
            mid=lis[i]
            lis[i]=lis[j]
            lis[j]=mid
        else:
            count=count+1
print(lis[0],lis[1]," OR ",lis[1],lis[0])
