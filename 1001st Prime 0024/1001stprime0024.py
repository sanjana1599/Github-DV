n=1
count=1
flag=True
f=0
while flag == True:
    n=n+2
    f=0
    for i in range (2,(n//2)+1):
        if n%i == 0:
            f=1 #not prime
            break
    if f == 0: #it is prime
        count=count+1
        if count == 1001:
            flag=False
print(n)
