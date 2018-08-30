a=1
b=1
st=0
sum=0
x=0
while a <= 100:
    f=a*b
    b=f
    a=a+1
x=b
while x != 0:
    last=x%10
    sum=sum+last
    full=x//10
    x=full
print (sum)
