sum=0
sqr=0
for i in range (1,101):
    a=i**2
    sqr=sqr+a
    sum=sum+i
sum=sum**2
ans=sum-sqr
print(ans)
