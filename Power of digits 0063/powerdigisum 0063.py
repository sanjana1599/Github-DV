x=1000
n=2**1000
print(n)
sum=0
while n!=0:
    last=n%10
    sum=sum+last
    full=n//10
    n=full
print (sum)
