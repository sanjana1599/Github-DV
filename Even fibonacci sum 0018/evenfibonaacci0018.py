mid=0
a=0
b=1
flag=True
sum=0
while a < 4000000:
    mid=a
    a=b
    b=mid+b
    if a%2 == 0:
        sum=sum+a
print(sum)
