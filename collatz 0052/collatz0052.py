num=1
n=0
count=1
finalcount=0
finaln=0
while num < 999998:
    num=num+2
    n=num
    count=1
    while n > 1:
        if n%2 == 0:
            n=n//2
            count=count+1
        else:
            n=(3*n)+1
            count=count+1
    if count > finalcount:
        finalcount=count
        finaln=num
print(finaln)
print(finalcount)
