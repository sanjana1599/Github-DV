n=1
g=0
sum=1
while n < (1001**2):
    g=g+2
    for i in range(0,4):
        n=n+g
        sum=sum+n
print(n)
print(sum)
