f=0
a=0
b=1
flag=True
while flag==True:
    mid=a
    a=b
    b=mid+b
    f=f+1
    if len(str(a))==1000:
        flag=False
        break
print (f)
print (a)
